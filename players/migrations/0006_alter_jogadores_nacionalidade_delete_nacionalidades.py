# Generated by Django 5.0.1 on 2024-01-19 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nationalities', '0001_initial'),
        ('players', '0005_nacionalidades_alter_jogadores_nacionalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogadores',
            name='nacionalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nationalities.nacionalidades'),
        ),
        migrations.DeleteModel(
            name='Nacionalidades',
        ),
    ]