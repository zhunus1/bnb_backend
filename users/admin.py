from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    AppUser,
)

class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['email', 'name', 'phone', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'phone') 
    ordering = ('email',)

admin.site.register(AppUser, AppUserAdmin)
