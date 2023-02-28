from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from products.models import Product, Notification

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    owner_slug = serializers.SlugField(source='owner.slug')
    date = serializers.DateTimeField(format='%d %b %Y')
    main_image = serializers.CharField(source='main_image.url')

    class Meta:
        model = Product
        fields = ['name', 'slug', 'owner', 'owner_slug', 'price', 'date', 'stars', 'main_image']

class NotificationSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d %b %Y')
    product_owner = serializers.SlugField(source='product.owner.slug')
    product_slug = serializers.SlugField(source='product.slug')
    image = serializers.CharField(source='product.main_image.url')

    class Meta:
        model = Notification
        fields = ['message', 'date', 'product_owner', 'product_slug', 'image',]