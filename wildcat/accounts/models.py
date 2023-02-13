from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models

from .managers import UserManager

# Create your models here.


class User(AbstractUser):
    is_premium = models.BooleanField(default=False)
    slug = models.SlugField()
    first_name = None
    last_name = None

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)