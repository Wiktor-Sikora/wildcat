# Generated by Django 4.1.7 on 2023-02-27 16:35


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_comment_dislikes_comment_likes_alter_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date']},
        ),
    ]
