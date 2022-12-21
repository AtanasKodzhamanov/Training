# Generated by Django 4.1.2 on 2022-12-21 03:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
