# Generated by Django 4.1.7 on 2023-02-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_timestamp_notification_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='redirect',
            new_name='product',
        ),
    ]
