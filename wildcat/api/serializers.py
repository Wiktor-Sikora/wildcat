from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    owner_slug = serializers.SlugField(source='owner.slug')
    date = serializers.DateTimeField(format='%d %b %Y')
    main_image = serializers.CharField(source='main_image.url')

    class Meta:
        model = Product
        fields = ['name', 'slug', 'owner', 'owner_slug', 'price', 'date', 'stars', 'main_image']