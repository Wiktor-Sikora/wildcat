# Generated by Django 4.1.6 on 2023-02-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]