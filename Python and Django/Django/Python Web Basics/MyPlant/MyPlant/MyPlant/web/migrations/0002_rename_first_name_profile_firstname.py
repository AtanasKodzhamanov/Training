# Generated by Django 4.1.2 on 2022-12-21 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='firstname',
        ),
    ]