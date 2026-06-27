from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Branch, Product, Supplier, Supply, WriteOff, EmployeeBadge

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'fullname', 'role', 'branch', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'fullname', 'branch')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'fullname', 'branch')}),
    )

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'latitude', 'longitude']
    search_fields = ['name', 'city']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sku', 'unit_type', 'unit_price']
    search_fields = ['name', 'sku']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contacts', 'ai_rating']
    search_fields = ['name']

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'branch', 'date']
    list_filter = ['supplier', 'branch']

@admin.register(WriteOff)
class WriteOffAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'branch', 'product', 'reason', 'quantity', 'status', 'created_at']
    list_filter = ['status', 'reason', 'branch']
    search_fields = ['product__name', 'employee__username']

@admin.register(EmployeeBadge)
class EmployeeBadgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'badge_name', 'date_received']
    list_filter = ['badge_name']

admin.site.register(User, CustomUserAdmin)
