from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User give email and password and extra_fields
        """
        if not email:
            raise ValueError(_("The Please Enter Email Address"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.last_name = self.
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser give email and password and extra_field
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    email = models.EmailField(_('آدرس ایمیل'), max_length=255, unique=True)
    username = models.CharField(_('نام کاربری '), max_length=50, unique=True)
    persons_id = models.CharField(_('شماره پرسنلی'), max_length=11, unique=True)
    first_name = models.CharField(_('نام'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('نام خانوادگی'), max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(_('کارمندان'), default=False)
    is_active = models.BooleanField(_('فعال'), default=False)
    is_superuser = models.BooleanField(_('مدیر'), default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.email