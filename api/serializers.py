# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import User, Outlet, WriteOffRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'role')


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ('id', 'name', 'address')


class WriteOffRequestSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    outlet_details = OutletSerializer(source='outlet', read_only=True)
    responsible_user_details = UserSerializer(source='responsible_user', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = WriteOffRequest
        fields = (
            'id', 'outlet', 'outlet_details', 'author', 'photo', 
            'type', 'type_display', 'responsible_user', 'responsible_user_details', 
            'comment', 'status', 'status_display', 'iiko_act_id', 
            'created_at', 'updated_at'
        )
        read_only_fields = ('status', 'iiko_act_id', 'created_at', 'updated_at')

    def validate_comment(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Комментарий должен содержать не менее 10 символов.")
        return value

    def validate(self, attrs):
        write_off_type = attrs.get('type', 'no_deduction')
        responsible_user = attrs.get('responsible_user', None)

        if write_off_type == 'with_deduction' and not responsible_user:
            raise serializers.ValidationError({
                "responsible_user": "Для списания с удержанием необходимо указать сотрудника."
            })
        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['author'] = request.user
        return super().create(validated_data)
