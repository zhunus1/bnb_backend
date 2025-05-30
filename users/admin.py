from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    AppUser,
)

class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['email', 'name', 'phone', 'is_staff', 'is_active', 'profile_type']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'profile_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone', 'is_staff', 'is_active', 'profile_type')}
        ),
    )
    search_fields = ('email', 'phone') 
    ordering = ('email',)
admin.site.register(AppUser, AppUserAdmin)
