from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from taggit.models import TaggedItemBase, TagBase
from taggit.managers import TaggableManager

from common.utils.texts import unique_slugify
from common.openai.openai_completion import open_ai_completion
# from common.synonyms import findsynonyms


User = get_user_model()

# Create your models here.

class Product(models.Model, HitCountMixin):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    _original_description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True)
    stars = models.ManyToManyField(User, related_name='stars')
    tags = TaggableManager(blank=True)
    main_image = models.ImageField(upload_to='products/', default='products/default.jpg', null=True, blank=False)
    
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.name)

    def save(self, *args, run_open_ai=False, **kwargs):    
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        self.modified = timezone.now()
        super(Product, self).save(*args, **kwargs)

        if run_open_ai:
            if self.description != self._original_description:
                tags, needs = open_ai_completion(self.description)
                for tag in tags:
                    self.tags.add(tag)
                for need in needs:
                    Needs.objects.create(text=need, product=self)
                
            self._original_description = self.description
            super(Product, self).save(*args, **kwargs)

            self.check_if_needs_available()
            self.check_for_product_needs()

    def check_for_product_needs(self):
        '''Searches for products that need this product'''
        needs = Needs.objects.filter(text__icontains=self.name)
        for need in needs:
            Notification.objects.create(message='Product that you need has been found', product=self, user=need.product.owner)

    def check_if_needs_available(self):
        '''looking for products that have needs'''
        needs = Needs.objects.filter(product=self.pk)
        for need in needs:
            available_products = Product.objects.filter(name__icontains=need)
            for product in available_products:
                Notification.objects.create(message='Product that you need has been found', product=product.pk, user=self.owner.pk)

class Needs(models.Model):
    text = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
            
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

    def __str__(self):
        return self.content

class Notification(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)