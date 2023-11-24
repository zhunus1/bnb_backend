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
    StartUpProfileCreateUpdateSerializer,
    InvestorProfileCreateUpdateSerializer,
    InvestorProfileDetailSerializer,
    InvestFundProfileCreateUpdateSerializer,
    InvestFundProfileDetailSerializer,
    CorporationProfileCreateUpdateSerializer,
    CorporationProfileDetailSerializer,
    SpecialistProfileCreateUpdateSerializer,
    SpecialistProfileDetailSerializer
)

# Create your views here.
class StartUpProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StartUpProfileCreateUpdateSerializer
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
        if self.action in ['create', 'update', 'partial_update']:
            return InvestorProfileCreateUpdateSerializer
        else:
            return InvestorProfileDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Investor.objects.filter(user = self.request.user)


class InvestFundProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return InvestFundProfileCreateUpdateSerializer
        else:
            return InvestFundProfileDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return InvestFund.objects.filter(user = self.request.user)


class CorporationProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CorporationProfileCreateUpdateSerializer
        else:
            return CorporationProfileDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Corporation.objects.filter(user = self.request.user)
    

class SpecialistProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SpecialistProfileCreateUpdateSerializer
        else:
            return SpecialistProfileDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Specialist.objects.filter(user = self.request.user)
