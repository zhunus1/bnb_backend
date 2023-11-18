# yourapp/urls.py
from django.urls import path
from .views import (
    CodeRequestAPIView,
    RegistrationAPIView,
    PasswordResetConfirmAPIView,
    VerificationAPIView,
    LoginAPIView,
)

urlpatterns = [
    path('code/request/', CodeRequestAPIView.as_view(), name='code_request'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('password/reset/confirm/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
    path('verification/', VerificationAPIView.as_view(), name='verification'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
