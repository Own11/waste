# pyrefly: ignore [missing-import]
from rest_framework import status, permissions, views
# pyrefly: ignore [missing-import]
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count, Q
from django.utils import timezone
from decimal import Decimal
import logging
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.views import TokenObtainPairView
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Branch, Product, Supplier, Supply, WriteOff, EmployeeBadge
from .serializers import (
    UserSerializer, BranchSerializer, ProductSerializer, 
    SupplierSerializer, SupplySerializer, WriteOffSerializer, EmployeeBadgeSerializer
)
from .services import RoboflowService, OpenAIService

logger = logging.getLogger(__name__)

# --- CUSTOM JWT AUTH ---

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        data['username'] = self.user.username
        data['fullname'] = self.user.fullname
        data['user_id'] = self.user.id
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# --- SHARED RESOURCE VIEWS ---

class ProductsListView(views.APIView):
    """Returns all products available for write-off selection."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all().order_by('name')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class BranchesListView(views.APIView):
    """Returns all branches (for dropdowns)."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        branches = Branch.objects.all().order_by('name')
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)


# --- CUSTOM PERMISSION GUARDS ---

class IsWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'worker'


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsManagerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['manager', 'admin']


# --- WORKER VIEWS ---

class WorkerProfileView(views.APIView):
    permission_classes = [IsWorker]

    def get(self, request):
        user = request.user
        # Collect statistics
        approved_count = WriteOff.objects.filter(employee=user, status='approved').count()
        rejected_count = WriteOff.objects.filter(employee=user, status='rejected').count()
        total_count = WriteOff.objects.filter(employee=user).count()
        
        badges = EmployeeBadge.objects.filter(employee=user)
        badge_serializer = EmployeeBadgeSerializer(badges, many=True)
        
        # Call OpenAI tips service
        ai_tips = OpenAIService.generate_employee_tips(user.id)
        
        user_serializer = UserSerializer(user)
        
        return Response({
            "profile": user_serializer.data,
            "statistics": {
                "total_write_offs": total_count,
                "approved_write_offs": approved_count,
                "rejected_write_offs": rejected_count,
                "accuracy_rate_percent": round((approved_count / total_count * 100), 1) if total_count > 0 else 100.0
            },
            "badges": badge_serializer.data,
            "ai_recommendations": ai_tips
        })


class WorkerScanView(views.APIView):
    permission_classes = [IsWorker]

    def post(self, request):
        photo = request.FILES.get('photo')
        if not photo:
            return Response({"error": "Фотография обязательна для распознавания."}, status=status.HTTP_400_BAD_REQUEST)
            
        # Run Roboflow image processing scan
        result = RoboflowService.scan_image(photo)
        if not result.get('success'):
            return Response({"error": result.get('error', 'Ошибка распознавания.')}, status=status.HTTP_502_BAD_GATEWAY)
            
        return Response(result)


class WorkerWriteOffCreateView(views.APIView):
    permission_classes = [IsWorker]

    def post(self, request):
        product_id = request.data.get('product')
        quantity_str = request.data.get('quantity')
        reason = request.data.get('reason')
        photo = request.FILES.get('photo')
        ai_confidence = request.data.get('ai_confidence', 0.0)

        if not product_id or not quantity_str or not reason:
            return Response({"error": "Поля product, quantity, и reason обязательны."}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, pk=product_id)
        branch = request.user.branch

        if not branch:
            return Response({"error": "Сотрудник не привязан ни к одному филиалу."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quantity = Decimal(str(quantity_str))
            if quantity <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return Response({"error": "Неверное количество товара."}, status=status.HTTP_400_BAD_REQUEST)

        write_off = WriteOff.objects.create(
            employee=request.user,
            branch=branch,
            product=product,
            photo=photo,
            ai_confidence=float(ai_confidence),
            reason=reason,
            quantity=quantity,
            status='pending'
        )

        serializer = WriteOffSerializer(write_off, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# --- MANAGER / ADMIN VIEWS ---

class ManagerRequestsListView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request):
        # Fetch only write-offs that are pending review
        queryset = WriteOff.objects.filter(status='pending').order_by('created_at')
        serializer = WriteOffSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class ManagerReviewView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def patch(self, request, pk):
        write_off = get_object_or_404(WriteOff, pk=pk)
        
        if write_off.status != 'pending':
            return Response({"error": "Заявка уже обработана."}, status=status.HTTP_400_BAD_REQUEST)
            
        review_action = request.data.get('action')
        if not review_action or review_action not in ['approve', 'reject']:
            return Response({"error": "Параметр 'action' должен быть 'approve' или 'reject'."}, status=status.HTTP_400_BAD_REQUEST)
            
        if review_action == 'approve':
            write_off.status = 'approved'
            # Simulating stock inventory reduction logic
            logger.info(f"Inventory reduction simulation: product {write_off.product.name} (SKU: {write_off.product.sku}), qty: {write_off.quantity} deducted from stock at {write_off.branch.name}.")
        else:
            write_off.status = 'rejected'
            
        write_off.manager = request.user
        write_off.updated_at = timezone.now()
        write_off.save()
        
        serializer = WriteOffSerializer(write_off, context={'request': request})
        return Response(serializer.data)


class ManagerSupplyCheckView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def post(self, request):
        supplier_id = request.data.get('supplier')
        branch_id = request.data.get('branch')
        date_str = request.data.get('date')
        photo = request.FILES.get('photo')

        if not supplier_id or not branch_id or not date_str:
            return Response({"error": "Поля supplier, branch, и date обязательны."}, status=status.HTTP_400_BAD_REQUEST)

        supplier = get_object_or_404(Supplier, pk=supplier_id)
        branch = get_object_or_404(Branch, pk=branch_id)

        try:
            date_parsed = timezone.datetime.fromisoformat(date_str)
        except ValueError:
            return Response({"error": "Неверный формат даты. Используйте ISO формат."}, status=status.HTTP_400_BAD_REQUEST)

        photos_list = []
        if photo:
            # Storing filenames as simple list representation
            photos_list.append(photo.name)

        # Create Supply record
        supply = Supply.objects.create(
            supplier=supplier,
            branch=branch,
            date=date_parsed,
            photos=photos_list
        )

        # Execute AI analysis report
        ai_report = OpenAIService.analyze_supplier_delivery(supply.id)
        
        # Re-fetch with updated values
        supply.refresh_from_db()
        serializer = SupplySerializer(supply, context={'request': request})
        
        return Response({
            "supply": serializer.data,
            "ai_analysis": ai_report,
            "supplier_new_ai_rating": supplier.ai_rating
        }, status=status.HTTP_201_CREATED)


class ManagerSuppliersListView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request):
        suppliers = Supplier.objects.all()
        result = []
        
        for s in suppliers:
            # Calculate Volume (number of supplies)
            volume = s.supplies.count()
            
            # Count complaints (Supplies with defect rate > 5.0%)
            complaints = 0
            for supply in s.supplies.all():
                rep = supply.ai_status_report
                if isinstance(rep, dict) and rep.get('defect_rate_percent', 0) > 5.0:
                    complaints += 1
            
            # Calculate Losses (cost of write-offs due to supplier defect)
            losses_queryset = WriteOff.objects.filter(
                status='approved',
                reason='supplier_defect',
                product__in=Product.objects.all() # Simple association fallback
            )
            
            # Aggregate total losses sum for supplier products
            total_losses = 0.0
            for wo in losses_queryset:
                total_losses += float(wo.quantity) * float(wo.product.unit_price)
            
            # In a real environment, products would be linked to suppliers. 
            # We mock the loss distribution if no products are explicitly tied.
            # E.g., distribute losses dynamically
            supplier_share_factor = {
                "FreshFood": 0.4,
                "AgroLine": 0.3,
                "Baker Pro": 0.2,
                "Qazaq Dairy": 0.1
            }.get(s.name, 0.2)
            
            supplier_losses = round(total_losses * supplier_share_factor, 2)

            result.append({
                "id": s.id,
                "name": s.name,
                "contacts": s.contacts,
                "ai_rating": s.ai_rating,
                "volume": volume,
                "complaints": complaints,
                "losses_tenge": supplier_losses
            })
            
        return Response(result)


# --- EXECUTIVE / ANALYTICS VIEWS ---

class AnalyticsDashboardView(views.APIView):
    permission_classes = [IsManagerOrAdmin] # Manager/Admin acts as Executive in MVP

    def get(self, request):
        # 1. Total network losses
        approved_write_offs = WriteOff.objects.filter(status='approved')
        total_losses = sum(float(wo.quantity) * float(wo.product.unit_price) for wo in approved_write_offs)

        # 2. Losses by branch
        branches = Branch.objects.all()
        losses_by_branch = []
        for b in branches:
            branch_wos = approved_write_offs.filter(branch=b)
            val = sum(float(wo.quantity) * float(wo.product.unit_price) for wo in branch_wos)
            losses_by_branch.append({
                "branch_id": b.id,
                "branch_name": b.name,
                "city": b.city,
                "losses_tenge": round(val, 2)
            })

        # 3. Losses by employee
        employees = User.objects.filter(role='worker')
        losses_by_employee = []
        for emp in employees:
            emp_wos = approved_write_offs.filter(employee=emp)
            val = sum(float(wo.quantity) * float(wo.product.unit_price) for wo in emp_wos)
            losses_by_employee.append({
                "employee_id": emp.id,
                "username": emp.username,
                "fullname": emp.fullname,
                "losses_tenge": round(val, 2)
            })

        # 4. Generate AI daily insights and forecasts
        ai_insights = OpenAIService.root_cause_and_forecasting()

        return Response({
            "total_losses_tenge": round(total_losses, 2),
            "losses_by_branch": losses_by_branch,
            "losses_by_employee": losses_by_employee,
            "prevented_losses_tenge": ai_insights.get("prevented_losses_tenge", 0.0),
            "forecast_losses_next_month_tenge": ai_insights.get("forecast_losses_next_month_tenge", 0.0),
            "ai_daily_insight": ai_insights.get("ai_daily_insight", ""),
            "root_cause_summary": ai_insights.get("root_cause_summary", "")
        })


class AnalyticsHeatmapView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request):
        approved_write_offs = WriteOff.objects.filter(status='approved')
        branches = Branch.objects.all()
        result = []
        
        for b in branches:
            branch_wos = approved_write_offs.filter(branch=b)
            val = sum(float(wo.quantity) * float(wo.product.unit_price) for wo in branch_wos)
            
            # Categorize based on limits
            # Green: < 50k, Yellow: 50k - 150k, Red: >= 150k
            if val < 50000:
                color = "green"
            elif val < 150000:
                color = "yellow"
            else:
                color = "red"
                
            result.append({
                "branch_id": b.id,
                "branch_name": b.name,
                "city": b.city,
                "coordinates": {
                    "lat": b.latitude,
                    "lng": b.longitude
                },
                "total_losses_tenge": round(val, 2),
                "status_color": color
            })
            
        return Response(result)


class AnalyticsExportSheetsView(views.APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request):
        # Build mock data structure for spreadsheet integration
        approved_write_offs = WriteOff.objects.filter(status='approved')
        export_rows = []
        
        for wo in approved_write_offs:
            cost = float(wo.quantity) * float(wo.product.unit_price)
            export_rows.append({
                "Date": wo.created_at.strftime("%Y-%m-%d %H:%M"),
                "Branch": wo.branch.name,
                "City": wo.branch.city,
                "Employee": wo.employee.fullname or wo.employee.username,
                "Product": wo.product.name,
                "Quantity": float(wo.quantity),
                "Unit Price": float(wo.product.unit_price),
                "Total Cost": cost,
                "Reason": wo.get_reason_display()
            })
            
        return Response({
            "status": "Success",
            "message": "Данные успешно выгружены для Google Sheets.",
            "exported_at": timezone.now().isoformat(),
            "spreadsheet_name": f"Write-Offs Analytics Network_{timezone.now().strftime('%Y%m%d')}",
            "mock_url": "https://docs.google.com/spreadsheets/d/1MockSpreadsheetIDForMentoriaHackathon2026/edit",
            "rows_count": len(export_rows),
            "data": export_rows
        })
