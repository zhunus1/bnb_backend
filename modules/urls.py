from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StartUpStageViewSet,
    IndustryViewSet,
    BussinessModelViewSet,
    TechnologyViewSet,
    SellingModelViewSet,
    CountryViewSet,
    InnovationMethodViewSet,
    InvestRoundViewSet
)

router = DefaultRouter()
router.register(r'startup-stages', StartUpStageViewSet, basename='startup-stages')
router.register(r'industries', IndustryViewSet, basename='industries')
router.register(r'bussiness-models', BussinessModelViewSet, basename='bussiness-models')
router.register(r'technologies', TechnologyViewSet, basename='technologies')
router.register(r'selling-models', SellingModelViewSet, basename='selling-models')
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'innovation-methods', InnovationMethodViewSet, basename='innovation-methods')
router.register(r'invest-rounds', InvestRoundViewSet, basename='invest-rounds')


urlpatterns = [
    path('', include(router.urls)),
]