from django.contrib import admin

from .models import Product, Image, Notification, Needs, Comment

# Register your models here.

admin.site.register(Needs)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Notification)
admin.site.register(Comment)