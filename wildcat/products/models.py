from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(null=True)
    slug = models.SlugField(max_length=30, unique=True, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name} {self.id}')
        self.modified = timezone.now()
        super(Product, self).save(*args, **kwargs)
        

class Image(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, null=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
