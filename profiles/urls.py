from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.profile_views import (
    StartUpProfileViewSet,
    InvestorProfileViewSet,
    InvestFundProfileViewSet,
    CorporationProfileViewSet,
    SpecialistProfileViewSet
)
from .views.client_views import (
    StartUpViewSet,
    InvestorViewSet,
    InvestFundViewSet,
    CorporationViewSet,
    SpecialistViewSet   
)


visitor_router = DefaultRouter()
visitor_router.register(r'startups', StartUpViewSet, basename='startups')
visitor_router.register(r'investors', InvestorViewSet, basename='investors')
visitor_router.register(r'invest-funds', InvestFundViewSet, basename='invest-funds')
visitor_router.register(r'corporations', CorporationViewSet, basename='corporations')
visitor_router.register(r'specialists', SpecialistViewSet, basename='specialists')


profiles_router = DefaultRouter()
profiles_router.register(r'startups', StartUpProfileViewSet, basename='startups')
profiles_router.register(r'investors', InvestorProfileViewSet, basename='investors')
profiles_router.register(r'invest-funds', InvestFundProfileViewSet, basename='invest-funds')
profiles_router.register(r'corporations', CorporationProfileViewSet, basename='corporations')
profiles_router.register(r'specialists', SpecialistProfileViewSet, basename='specialists')

urlpatterns = [
    path('visitors/', include(visitor_router.urls)),
    path('users/', include(profiles_router.urls)),
]