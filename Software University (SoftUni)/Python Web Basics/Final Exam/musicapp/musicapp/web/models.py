from django.db import models
from django.core import validators


# Create your models here.
    # • Profile
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            validators.RegexValidator(r'^[a-zA-Z0-9_]+$', message='Ensure this value contains only letters, numbers, and underscore.')
        )
        )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=True,
        blank=True
        )

class Album(models.Model):
    album_name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    artist = models.CharField(max_length=30, null=False, blank=False)
    genre = models.CharField(max_length=30,null=False,blank=False, choices=(
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ))
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        ),
    )