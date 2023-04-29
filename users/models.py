from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_created_date = models.DateTimeField(auto_now_add=True)
    user_update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    email = models.EmailField(_('Email Address'), max_length=255, unique=True)
    username = models.CharField(_('User Name'), max_length=50, unique=True)
    first_name = models.CharField(_('First Name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(_('Is Staff'), default=False)
    is_active = models.BooleanField(_('Is Active'), default=False)
    is_superuser = models.BooleanField(_('Super User'), default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.email