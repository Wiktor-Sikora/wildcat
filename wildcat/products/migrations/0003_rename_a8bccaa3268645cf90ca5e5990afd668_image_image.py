# Generated by Django 4.1.6 on 2023-02-06 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='a8bccaa3268645cf90ca5e5990afd668',
            new_name='image',
        ),
    ]