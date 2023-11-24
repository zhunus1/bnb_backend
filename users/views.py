import time
import random
import redis
import string
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from users.models import (
    AppUser,
)
from .serializers import (
    RegistrationSerializer,
    VerificationSerializer,
    LoginSerializer,
    CodeRequestSerializer,
    PasswordResetSerializer
)

redis_instance = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
VERIFICATION_CODE_TIMEOUT = 5 * 60  # 5 minutes in seconds

class CodeRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):

        serializer = CodeRequestSerializer(
            data = request.data,
        )
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            try:
                user = AppUser.objects.get(email=email)
            except AppUser.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Generate a unique verification code
            while True:
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not cache.get(code):
                    break

            # Set the code in the cache with the user's ID and the specified timeout
            cache.set(code, user.id, timeout=VERIFICATION_CODE_TIMEOUT)
            
            # Send verification code to user's email
            subject = 'Код верификации почты'
            message = f'Your verification code is: {code}'
            from_email = 'bnbinfodesk@gmail.com'
            to_email = user.email

            try:
                send_mail(subject, message, from_email, [to_email])
                return Response({'detail': 'Verification code is sent. Check your email for verification code.'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Handle email sending failure
                cache.delete(code)  # Remove the code from cache if sending email fails
                return Response({'detail': f'Failed to send verification email. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Check if a user with the same email already exists
            if AppUser.objects.filter(email = email).exists():
                return Response({'detail': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
            return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data['code']
            password = serializer.validated_data['password']

            # Check if the reset code exists in the cache
            user_id = cache.get(code)

            if user_id is None:
                return Response({'detail': 'Invalid or expired reset code.'}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the user from the database
            user = AppUser.objects.get(id=user_id)

            # Update the user's password
            user.set_password(password)
            user.save()

            # Optionally, remove the reset code from the cache
            cache.delete(code)

            return Response({'detail': 'Password successfully reset.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerificationSerializer(
            data = request.data,
        )

        if serializer.is_valid():
            code = serializer.validated_data['code']

            # Check if the code exists in the cache
            user_id = cache.get(code)

            if user_id is None:
                return Response({'detail': 'Invalid or expired verification code.'}, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve the user from the database
            user = AppUser.objects.get(
                id = user_id,
            )

            if user.is_active:
                return Response({'detail': 'User is already verified.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Mark the user as verified (example: set a flag in the user model)
            user.is_active = True
            user.save()

            # Optionally, remove the verification code from the cache
            cache.delete(code)

            return Response({'detail': 'User successfully verified.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(
                request,
                email=email,
                password=password
            )

            if user:
                if user.is_active:
                    # Generate or get an existing token for the user
                    token, created = Token.objects.get_or_create(
                        user = user
                    )

                    # Optionally, you can include additional user information in the response
                    user_data = {
                        'id': user.id,
                        'email': user.email,
                    }

                    return Response({'token': token.key, 'user': user_data}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'User account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


