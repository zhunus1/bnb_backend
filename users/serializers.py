from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = (
            'id', 
            'email', 
            'name', 
            'phone_number', 
        )

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = (
            'name', 
            'email', 
            'phone_number', 
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def create(self, validated_data):
        """
        Create and return a new `AppUser` instance, given the validated data.
        """
        # Extract the password from the validated data
        password = validated_data.pop('password', None)

        # Create a new AppUser instance with the remaining data
        user = AppUser(**validated_data)

        # Set the password using the set_password method for proper hashing
        if password:
            user.set_password(password)

        # Save the user to the database
        user.save()

        return user

class VerificationSerializer(serializers.Serializer):
    code = serializers.CharField(
        max_length = 6, 
        required = True
    )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only = True,
    )


class PasswordResetSerializer(serializers.Serializer):
    code = serializers.CharField(
        max_length = 6, 
        required = True
    )
    password = serializers.CharField(
        write_only = True,
    )


class CodeRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()