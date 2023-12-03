from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.utils.translation import gettext as _
from rest_framework.authentication import TokenAuthentication
from ..models import (
   PilotProject,
   StartUp,
   Investor,
   InvestFund,
   Corporation,
   Specialist,
)
from ..serializers.profile_serializers import (
    StartUpProfileDetailSerializer,
    StartUpProfileUpdateSerializer,
    StartUpProfileCreateSerializer,
    InvestorProfileCreateSerializer,
    InvestorProfileUpdateSerializer,
    InvestorProfileDetailSerializer,
    InvestFundProfileCreateSerializer,
    InvestFundProfileUpdateSerializer,
    InvestFundProfileDetailSerializer,
    CorporationProfileCreateSerializer,
    CorporationProfileUpdateSerializer,
    CorporationProfileDetailSerializer,
    SpecialistProfileUpdateSerializer,
    SpecialistProfileCreateSerializer,
    SpecialistProfileDetailSerializer
)

# Create your views here.
class StartUpProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return StartUpProfileCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return StartUpProfileUpdateSerializer
        else:
            return StartUpProfileDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return StartUp.objects.filter(user = self.request.user)


class InvestorProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return InvestorProfileCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return InvestorProfileUpdateSerializer
        else:
            return InvestorProfileDetailSerializer

    def get_queryset(self):
        return Investor.objects.filter(user = self.request.user)


class InvestFundProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return InvestFundProfileCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return InvestFundProfileUpdateSerializer
        else:
            return InvestFundProfileDetailSerializer

    def get_queryset(self):
        return InvestFund.objects.filter(user = self.request.user)


class CorporationProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return CorporationProfileCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CorporationProfileUpdateSerializer
        else:
            return CorporationProfileDetailSerializer
    
    def get_queryset(self):
        return Corporation.objects.filter(user = self.request.user)
    

class SpecialistProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return SpecialistProfileCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return SpecialistProfileUpdateSerializer
        else:
            return SpecialistProfileDetailSerializer

    def get_queryset(self):
        return Specialist.objects.filter(user = self.request.user)
