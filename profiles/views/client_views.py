from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
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

# Create your views here.
class StartUpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StartUp.objects.all()
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
        

class InvestorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Investor.objects.all()
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


class InvestFundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestFund.objects.all()
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


class CorporationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Corporation.objects.all()
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


class SpecialistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialist.objects.all()
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