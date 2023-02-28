from django.contrib import admin

from .models import Product, Image, Notification

# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Notification)