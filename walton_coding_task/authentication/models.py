from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone = models.IntegerField(unique=True, blank=True, null=True,)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=255)
    name = models.CharField(blank=True, null=True, max_length=255)
    is_staff = models.BooleanField(default=False, blank=False, null=False)
    is_customer = models.BooleanField(default=True, blank=False, null=False)
    is_seller = models.BooleanField(default=False, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
