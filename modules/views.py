from django.shortcuts import render
from rest_framework import viewsets
from django.utils.translation import activate
from modeltranslation.utils import get_language
from rest_framework.response import Response
from .models import (
    StartUpStage, 
    Industry, 
    BussinessModel, 
    Technology, 
    SellingModel, 
    Country, 
    InnovationMethod, 
    InvestStage
)
from .serializers import (
    StartUpStageSerializer,
    IndustrySerializer,
    BussinessModelSerializer,
    TechnologySerializer,
    SellingModelSerializer,
    CountrySerializer,
    InnovationMethodSerializer,
    InvestStageSerializer
)
from .translation import (
    StartUpStageTranslationOptions,
    IndustryTranslationOptions,
    BussinessModelTranslationOptions,
    TechnologyTranslationOptions,
    SellingModelTranslationOptions,
    CountryTranslationOptions,
    InnovationMethodModelTranslationOptions,
    InvestStageTranslationOptions
)
# Create your views here.
class StartUpStageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StartUpStageSerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = StartUpStageTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = StartUpStage.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IndustrySerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = IndustryTranslationOptions.fields  # Add more fields as needed
        # Use the activated language to filter the queryset based on translated fields
        queryset = Industry.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class BussinessModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BussinessModelSerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = BussinessModelTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = BussinessModel.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TechnologySerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = TechnologyTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Technology.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class SellingModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SellingModelSerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = SellingModelTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = SellingModel.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = CountryTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Country.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class InnovationMethodViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InnovationMethodSerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = InnovationMethodModelTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = InnovationMethod.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class InvestStageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InvestStageSerializer

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = InvestStageTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = InvestStage.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset