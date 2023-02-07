from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Image(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, null=False)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return str(self.name)