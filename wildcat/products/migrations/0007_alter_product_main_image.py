# Generated by Django 4.1.7 on 2023-02-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_producttag_alter_product_main_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, default='products/default.jpg', null=True, upload_to='products/'),
        ),
    ]