# Generated by Django 5.0.1 on 2024-01-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacionalidades',
            name='img',
            field=models.ImageField(unique=True, upload_to='static/img'),
        ),
    ]
