from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from modeltranslation.utils import get_language
from ..paginations import CustomPageNumberPagination
from ..models import (
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)
from ..serializers.client_serializers import (
    StartUpListSerializer,
    StartUpDetailSerializer,
    InvestorListSerializer,
    InvestorDetailSerializer,
    InvestFundListSerializer,
    InvestFundDetailSerializer,
    CorporationListSerializer,
    CorporationDetailSerializer,
    SpecialistListSerializer,
    SpecialistDetailSerializer,
)

from ..filters import (
    StartUpFilter,
    InvestorFilter,
    InvestFundFilter,
    CorporationFilter,
    SpecialistFilter
)

from ..translation import (
    PilotProjectTranslationOptions,
    StartUpTranslationOptions,
    InvestorTranslationOptions,
    InvestFundTranslationOptions,
    CorporationTranslationOptions,
    SpecialistTranslationOptions
)


# Create your views here.
class StartUpViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StartUpFilter
    search_fields = (
        'startup_name',
        'organization_name'
    )
    pagination_class = CustomPageNumberPagination 

    def get_serializer_class(self):
        if self.action == 'list':
            return StartUpListSerializer
        else:
            return StartUpDetailSerializer
        
    def get_queryset(self):
        current_language = get_language()        
        translated_fields = StartUpTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = StartUp.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset
        

class InvestorViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = InvestorFilter
    search_fields = (
        'contact_name',
    )
    pagination_class = CustomPageNumberPagination 
    
    def get_serializer_class(self):
        if self.action == 'list':
            return InvestorListSerializer
        else:
            return InvestorDetailSerializer
    
    def get_queryset(self):
        current_language = get_language()        
        translated_fields = InvestorTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Investor.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class InvestFundViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = InvestFundFilter
    search_fields = (
        'public_name',
        'contact_name',
        'organization_name'
    )
    pagination_class = CustomPageNumberPagination 

    def get_serializer_class(self):
        if self.action == 'list':
            return InvestFundListSerializer
        else:
            return InvestFundDetailSerializer
    

    def get_queryset(self):
        current_language = get_language()        
        translated_fields = InvestFundTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = InvestFund.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class CorporationViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CorporationFilter
    search_fields = (
        'public_name',
        'organization_name'
    )
    pagination_class = CustomPageNumberPagination 
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CorporationListSerializer
        else:
            return CorporationDetailSerializer
    
    def get_queryset(self):
        current_language = get_language()        
        translated_fields = CorporationTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Corporation.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset


class SpecialistViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SpecialistFilter
    search_fields = (
        'user__name',
    )
    pagination_class = CustomPageNumberPagination 
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SpecialistListSerializer
        else:
            return SpecialistDetailSerializer
    
    def get_queryset(self):
        current_language = get_language()        
        translated_fields = SpecialistTranslationOptions.fields  # Add more fields as needed

        # Use the activated language to filter the queryset based on translated fields
        queryset = Specialist.objects.filter(
            **{
                f"{field}_{''.join(current_language.split('-'))}__isnull": False
                for field in translated_fields
            }
        )
        return queryset