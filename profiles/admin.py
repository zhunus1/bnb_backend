from django.contrib import admin
from .models import (
    StartUp, 
    Investor, 
    InvestFund, 
    Corporation, 
    Specialist
)

# Register your models here.
@admin.register(StartUp)
class StartUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'startup_name', 'created', 'updated']
    search_fields = ['startup_name']
    list_filter = ['created', 'updated', 'stage', 'industries', 'technologies', 'bussiness_models', 'selling_models', 'countries', 'have_sellings', 'have_pilots', 'active_search']

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_name', 'created', 'updated']
    search_fields = ['contact_name']
    list_filter = ['created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

@admin.register(InvestFund)
class InvestFundAdmin(admin.ModelAdmin):
    list_display = ['id', 'public_name', 'created', 'updated']
    search_fields = ['public_name']
    list_filter = ['created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

@admin.register(Corporation)
class CorporationAdmin(admin.ModelAdmin):
    list_display = ['id', 'public_name', 'created', 'updated']
    search_fields = ['public_name']
    list_filter = ['created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated']
    search_fields = ['user__username', 'user__email']
    list_filter = ['created', 'updated', 'industries', 'technologies', 'information_source']