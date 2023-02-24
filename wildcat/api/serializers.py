from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    owner_slug = serializers.SlugField(source='owner.slug')
    date = serializers.DateTimeField(format='%d %b %Y')

    class Meta:
        model = Product
        fields = ['name', 'owner', 'owner_slug', 'price', 'date', 'stars', 'main_image']