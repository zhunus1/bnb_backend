from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    StartUpStage, 
    Industry, 
    BussinessModel, 
    Technology, 
    SellingModel, 
    Country, 
    InnovationMethod, 
    InvestRound
)
from .serializers import (
    StartUpStageSerializer,
    IndustrySerializer,
    BussinessModelSerializer,
    TechnologySerializer,
    SellingModelSerializer,
    CountrySerializer,
    InnovationMethodSerializer,
    InvestRoundSerializer
)

# Create your views here.
class StartUpStageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StartUpStage.objects.all()
    serializer_class = StartUpStageSerializer


class IndustryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class BussinessModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BussinessModel.objects.all()
    serializer_class = BussinessModelSerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class SellingModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SellingModel.objects.all()
    serializer_class = SellingModelSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class InnovationMethodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InnovationMethod.objects.all()
    serializer_class = InnovationMethodSerializer


class InvestRoundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestRound.objects.all()
    serializer_class = InvestRoundSerializer