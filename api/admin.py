from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Outlet, WriteOffRequest

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']

@admin.register(WriteOffRequest)
class WriteOffRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'outlet', 'author', 'type', 'status', 'iiko_act_id', 'created_at']
    list_filter = ['status', 'type', 'outlet']
    search_fields = ['comment', 'iiko_act_id']
    raw_id_fields = ['author', 'responsible_user']

admin.site.register(User, CustomUserAdmin)
