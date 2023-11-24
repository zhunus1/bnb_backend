from django.shortcuts import render
from rest_framework import viewsets
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

# Create your views here.
class StartUpViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StartUp.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StartUpListSerializer
        else:
            return StartUpDetailSerializer
        

class InvestorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Investor.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return InvestorListSerializer
        else:
            return InvestorDetailSerializer


class InvestFundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestFund.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return InvestFundListSerializer
        else:
            return InvestFundDetailSerializer


class CorporationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Corporation.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CorporationListSerializer
        else:
            return CorporationDetailSerializer


class SpecialistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialist.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SpecialistListSerializer
        else:
            return SpecialistDetailSerializer