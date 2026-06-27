# pyrefly: ignore [missing-import]
from rest_framework import viewsets, permissions, status
# pyrefly: ignore [missing-import]
from rest_framework.decorators import action
# pyrefly: ignore [missing-import]
from rest_framework.response import Response
# pyrefly: ignore [missing-import]
from rest_framework.authtoken.views import ObtainAuthToken
# pyrefly: ignore [missing-import]
from rest_framework.authtoken.models import Token

from .models import User, Outlet, WriteOffRequest
from .serializers import UserSerializer, OutletSerializer, WriteOffRequestSerializer
# pyrefly: ignore [missing-import]
from .services import IikoService

class ObtainAuthTokenWithRole(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'role': user.role,
            'first_name': user.first_name,
            'last_name': user.last_name
        })


class IsSenderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'sender'


class IsCheckerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'checker'


class OutletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outlet.objects.all().order_by('name')
    serializer_class = OutletSerializer
    permission_classes = [permissions.IsAuthenticated]


class SenderUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(role='sender').order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class WriteOffRequestViewSet(viewsets.ModelViewSet):
    serializer_class = WriteOffRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'checker':
            # Checkers see requests waiting for review (on_review)
            return WriteOffRequest.objects.filter(status='on_review')
        else:
            # Senders see their own created requests
            return WriteOffRequest.objects.filter(author=user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsSenderPermission()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Automatically set current user as author
        serializer.save(author=self.request.user)


class ReviewRequestViewSet(viewsets.ViewSet):
    permission_classes = [IsCheckerPermission]

    def list(self, request):
        queryset = WriteOffRequest.objects.filter(status='on_review')
        serializer = WriteOffRequestSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='review')
    def review(self, request, pk=None):
        try:
            write_off = WriteOffRequest.objects.get(pk=pk)
        except WriteOffRequest.DoesNotExist:
            return Response({"detail": "Заявка не найдена."}, status=status.HTTP_404_NOT_FOUND)

        if write_off.status != 'on_review':
            return Response(
                {"detail": f"Невозможно обработать заявку в статусе '{write_off.get_status_display()}'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        review_action = request.data.get('action')
        if not review_action or review_action not in ['approve', 'reject']:
            return Response(
                {"detail": "Параметр 'action' должен быть 'approve' или 'reject'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if review_action == 'approve':
            payload = {
                "request_id": write_off.id,
                "outlet_name": write_off.outlet.name,
                "type": write_off.type,
                "responsible_user": write_off.responsible_user.username if write_off.responsible_user else None,
                "comment": write_off.comment
            }
            try:
                iiko_response = IikoService.create_write_off_act(payload)
                if iiko_response.get('success'):
                    write_off.status = 'iiko_synced'
                    write_off.iiko_act_id = iiko_response.get('iiko_act_id')
                    write_off.save()
                else:
                    return Response(
                        {"detail": "Ошибка интеграции с iiko API."},
                        status=status.HTTP_502_BAD_GATEWAY
                    )
            except Exception as e:
                return Response(
                    {"detail": f"Исключение при вызове iiko: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        elif review_action == 'reject':
            write_off.status = 'rejected'
            write_off.save()

        serializer = WriteOffRequestSerializer(write_off, context={'request': request})
        return Response(serializer.data)
