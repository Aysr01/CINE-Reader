# Generated by Django 4.2.4 on 2023-08-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recto', models.ImageField(upload_to='static/')),
                ('Verso', models.ImageField(upload_to='static/')),
            ],
        ),
    ]