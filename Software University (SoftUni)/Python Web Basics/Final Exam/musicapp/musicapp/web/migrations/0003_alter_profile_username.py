# Generated by Django 4.1.2 on 2022-12-21 07:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_album_album_name_alter_album_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z0-9_]+$', message='Ensure this value contains only letters, numbers, and underscore.')]),
        ),
    ]
