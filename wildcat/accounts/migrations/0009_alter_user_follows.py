# Generated by Django 4.1.6 on 2023-02-22 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]