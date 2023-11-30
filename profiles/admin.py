from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationGenericTabularInline
from .models import (
    StartUp, 
    Investor, 
    InvestFund, 
    Corporation, 
    Specialist,
    PilotProject
)


# Register your models here.

class PilotProjectInline(TranslationGenericTabularInline):
    model = PilotProject


class StartUpAdmin(TranslationAdmin):
    list_display = ['id', 'startup_name', 'created', 'updated']
    search_fields = ['startup_name']
    list_filter = ['is_approved', 'created', 'updated', 'startup_stage', 'industries', 'technologies', 'bussiness_models', 'selling_models', 'countries', 'have_sellings', 'have_pilots', 'active_search']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(StartUp, StartUpAdmin)


class InvestorAdmin(TranslationAdmin):
    inlines = [
        PilotProjectInline,
    ]
    list_display = ['id', 'contact_name', 'created', 'updated']
    search_fields = ['contact_name']
    list_filter = ['is_approved', 'created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Investor, InvestorAdmin)


class InvestFundAdmin(TranslationAdmin):
    inlines = [
        PilotProjectInline,
    ]
    list_display = ['id', 'public_name', 'created', 'updated']
    search_fields = ['public_name']
    list_filter = ['is_approved', 'created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(InvestFund, InvestorAdmin)


class CorporationAdmin(TranslationAdmin):
    inlines = [
        PilotProjectInline,
    ]
    list_display = ['id', 'public_name', 'created', 'updated']
    search_fields = ['public_name']
    list_filter = ['is_approved', 'created', 'updated', 'country', 'methods', 'stage', 'technologies', 'industries', 'have_experience', 'is_investing', 'invest_rounds', 'geography']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Corporation, CorporationAdmin)


class SpecialistAdmin(TranslationAdmin):
    list_display = ['id', 'user', 'created', 'updated']
    search_fields = ['user__username', 'user__email']
    list_filter = ['is_approved', 'created', 'updated', 'industries', 'technologies', 'information_source']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Specialist, SpecialistAdmin)


class PilotProjectAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'description', 'created', 'updated']
    search_fields = ['title']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(PilotProject, PilotProjectAdmin)


