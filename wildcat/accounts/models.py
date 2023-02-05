from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import BaseUserManager

# Create your models here.


class User(AbstractUser):
    is_premium = models.BooleanField(default=False)
    first_name = None
    last_name = None

    objects = BaseUserManager()