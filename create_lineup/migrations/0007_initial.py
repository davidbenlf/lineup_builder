# Generated by Django 5.0.1 on 2024-01-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('create_lineup', '0006_delete_persond'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
