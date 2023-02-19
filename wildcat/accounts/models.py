from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models
from django.utils import timezone

from accounts.managers import UserManager

# Create your models here.


class User(AbstractUser):
    is_premium = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    modified = models.DateTimeField(null=True)
    first_name = None
    last_name = None

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.username))
        modified = timezone.now()
        super(User, self).save(*args, **kwargs)