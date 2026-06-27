# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import User, Branch, Product, Supplier, Supply, WriteOff, EmployeeBadge

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'city', 'latitude', 'longitude')


class UserSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'role', 'branch', 'branch_name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'unit_type', 'unit_price')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'contacts', 'ai_rating')


class SupplySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Supply
        fields = ('id', 'supplier', 'supplier_name', 'branch', 'branch_name', 'date', 'photos', 'ai_status_report')
        read_only_fields = ('ai_status_report',)


class WriteOffSerializer(serializers.ModelSerializer):
    employee_details = UserSerializer(source='employee', read_only=True)
    branch_details = BranchSerializer(source='branch', read_only=True)
    product_details = ProductSerializer(source='product', read_only=True)
    manager_details = UserSerializer(source='manager', read_only=True)
    reason_display = serializers.CharField(source='get_reason_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = WriteOff
        fields = (
            'id', 'employee', 'employee_details', 'branch', 'branch_details', 
            'product', 'product_details', 'photo', 'ai_confidence', 
            'reason', 'reason_display', 'quantity', 'status', 'status_display', 
            'manager', 'manager_details', 'created_at', 'updated_at'
        )
        read_only_fields = ('employee', 'branch', 'ai_confidence', 'status', 'manager', 'created_at', 'updated_at')


class EmployeeBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBadge
        fields = ('id', 'badge_name', 'date_received')
