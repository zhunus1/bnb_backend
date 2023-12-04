from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet,
    SupportTicketCreateView,
)


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')


urlpatterns = [
    path('', include(router.urls)),
    path('support/', SupportTicketCreateView.as_view(), name='support-create'),
]