from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Client, Licensing_modules


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_client', 'is_service', 'is_sales', 'is_demo', 'is_comtactadmin', 'is_api', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active', 'client', 'is_api')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'password', 'last_name', 'client')}),
        ('Permissions', {'fields': ('is_staff', 'is_client', 'is_service', 'is_sales', 'is_demo', 'is_comtactadmin', 'is_api', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_client', 'is_service', 'is_sales', 'is_demo', 'is_comtactadmin', 'is_api', 'is_active')}
        ),
    )
    search_fields = ('email', 'client',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Client)
admin.site.register(Licensing_modules)