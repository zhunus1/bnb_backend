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
    StartUpDetailSerializer,
    StartUpCreateUpdateSerializer,
    InvestorCreateUpdateSerializer,
    InvestorDetailSerializer,
    InvestFundCreateUpdateSerializer,
    InvestFundDetailSerializer,
    CorporationCreateUpdateSerializer,
    CorporationDetailSerializer,
    SpecialistCreateUpdateSerializer,
    SpecialistDetailSerializer
)

# Create your views here.
class StartUpProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StartUpCreateUpdateSerializer
        else:
            return StartUpDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return StartUp.objects.filter(user = self.request.user)


class InvestorProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return InvestorCreateUpdateSerializer
        else:
            return InvestorDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Investor.objects.filter(user = self.request.user)


class InvestFundProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return InvestFundCreateUpdateSerializer
        else:
            return InvestFundDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return InvestFund.objects.filter(user = self.request.user)


class CorporationProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CorporationCreateUpdateSerializer
        else:
            return CorporationDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Corporation.objects.filter(user = self.request.user)
    

class SpecialistProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SpecialistCreateUpdateSerializer
        else:
            return SpecialistDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Specialist.objects.filter(user = self.request.user)
