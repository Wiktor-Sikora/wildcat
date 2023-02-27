from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

from common.utils.texts import unique_slugify
from common.openai.openai import tager
from common.synonyms import findsynonyms

User = get_user_model()

# Create your models here.

class ProductTag(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(null=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model, HitCountMixin):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True)
    stars = models.ManyToManyField(User, related_name='stars')
    tags = models.ManyToManyField(ProductTag, related_name='tags')
    main_image = models.ImageField(upload_to='products/', default='products/default.jpg', null=True, blank=True)
    
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        self.modified = timezone.now()
        super(Product, self).save(*args, **kwargs)

        description = self.description
        dictionary = tager(input=description)
        dictionary = findsynonyms(input=dictionary)
        producttags = dictionary["tags"]
        producttags.append(dictionary["need"])

        for i in producttags:
            if ProductTag.objects.filter(name=i).exists():
                tag = ProductTag.objects.filter(name=i).first()
                tag.number = tag.number+1
            else:
                tag = ProductTag.objects.create(name=i, number=1)
            tag.save()
            self.tags.add(tag)
        
            
class Image(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, null=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)

    def __str__(self):
        return str(self.product.name)

class Comment(models.Model):
    content = models.TextField(max_length=1000, blank=False)
    product = models.ForeignKey(Product, models.CASCADE)
    author = models.ForeignKey(User, models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')