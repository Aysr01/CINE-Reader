# Generated by Django 4.2.4 on 2023-08-25 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine_reader', '0005_image_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='caption',
        ),
    ]
