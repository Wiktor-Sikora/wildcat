# Generated by Django 4.1.7 on 2023-02-28 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_notification_is_read_notification_redirect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='timestamp',
            new_name='date',
        ),
    ]
