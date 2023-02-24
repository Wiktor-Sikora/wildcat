from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone

from common.utils.texts import unique_slugify
from products.openai import tager

User = get_user_model()

# Create your models here.

class ProductTag(models.Model):
    name = models.CharField(max_length=30)
    disabled = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True)
    stars = models.ManyToManyField(User, related_name='stars')
    tags = models.ManyToManyField(ProductTag, related_name='tags')
    main_image = models.ImageField(upload_to='products/', default='products/empty.png', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        self.modified = timezone.now()
        super(Product, self).save(*args, **kwargs)

        description = self.description
        producttags = tager(input=description)
        for i in producttags:
            
            if ProductTag.objects.filter(name=i).exists():
                print('This tag is exist')
                tag = ProductTag.objects.filter(name=i).first()
            else:
                tag = ProductTag.objects.create(name=i)
                tag.save()
            self.tags.add(tag)
        
            
class Image(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, null=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)

    def __str__(self):
        return str(self.product.name)

class Comment(models.Model):
    content = models.CharField(max_length=200, blank=False)
    product = models.ForeignKey(Product, models.CASCADE)
    author = models.ForeignKey(User, models.CASCADE)
    date = models.DateTimeField(auto_now=True)