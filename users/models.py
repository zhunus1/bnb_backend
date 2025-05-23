from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
from django.db import models
from django.utils import timezone

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class AppUser(AbstractBaseUser, PermissionsMixin):
    PROFILE_CHOICES = [
        ('StartUp', 'StartUp'),
        ('Investor', 'Investor'),
        ('InvestFund', 'InvestFund'),
        ('Corporation', 'Corporation'),
        ('Specialist', 'Specialist'),
    ]

    email = models.EmailField(
        unique = True,
        verbose_name = _("Электронная почта"),
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = _("ФИО"),
    )
    phone = PhoneNumberField(
        verbose_name = _("Номер телефона"),
    )
    profile_type = models.CharField(
        max_length = 11,
        choices = PROFILE_CHOICES,
        verbose_name =_("Тип профиля"),
        null = True, 
        blank = True
    )
    is_active = models.BooleanField(
        default = False,
        verbose_name = _("Подтверждена почта?"),
    )
    is_staff = models.BooleanField(
        default = False,
        verbose_name = _("Администратор?"),
    )
    date_joined = models.DateTimeField(
        default = timezone.now,
        verbose_name = _("Дата регистрации"),
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
