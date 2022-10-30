from django.db import models
from django.core import validators, exceptions

# Create your models here.

def validate_string_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != "-":
            raise exceptions.ValidationError("Message")

class Profile(models.Model):
    MIN_LEN_USERNAME=2
    MAX_LEN_USERNAME=15

    username=models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validate_string_alphanumeric,
        ),
        null=False,
        blank=False,
    )

    email=models.EmailField(
        null=False,
        blank=False,
    )

    age=models.PositiveIntegerField(
        null=True,
        blank=True,
    )

class Album(models.Model):
    MAX_LEN_NAME=30
    MAX_LEN_ARTIST=30
    MAX_LEN_GENRE=30

    POP_MUSIC="Pop Music"
    JAZZ_MUSIC="Jazz Music"
    RNB_MUSIC="R&B Music"
    ROCK_MUSIC="Rock Music"
    COUNTRY_MUSIC="Country Music"
    DANCE_MUSIC="Dance Music"
    HIPHOP_MUSIC="Hip Hop Music"
    OTHER="Other"

    MUSICS=(
        (POP_MUSIC,POP_MUSIC),
        (JAZZ_MUSIC,JAZZ_MUSIC),
        (RNB_MUSIC,RNB_MUSIC),
        (ROCK_MUSIC,ROCK_MUSIC),
        (COUNTRY_MUSIC,COUNTRY_MUSIC),
        (DANCE_MUSIC,DANCE_MUSIC),
        (OTHER,OTHER),
        (HIPHOP_MUSIC,HIPHOP_MUSIC)
    )

    album_name=models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
    )

    artist=models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        null=False,
        choices=MUSICS,
        blank=False,

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False, 
        validators=(
            validators.MinValueValidator(0.00),
        ),
    )

