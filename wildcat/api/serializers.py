from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')

    class Meta:
        model = Product
        fields = ['name', 'owner', 'price', 'date', 'stars', 'main_image']