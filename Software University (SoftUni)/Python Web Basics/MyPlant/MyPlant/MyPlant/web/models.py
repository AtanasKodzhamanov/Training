from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


# Create your models here.
class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    FIRSTNAME_MAX_LENGTH = 20
    LASTNAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)]
    )

    firstname = models.CharField(
        max_length=FIRSTNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[validate_name])

    last_name = models.CharField(
        max_length=LASTNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[validate_name])
        
    profile_picture = models.URLField(
        null=True,
        blank=True
    )

class Plant(models.Model):
    PLANTTYPE_MAX_LENGTH = 14
    NAME_MAX_LENGTH = 20

    PLANT_TYPE_CHOICES = [
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    ]
    plant_type = models.CharField(
        max_length=PLANTTYPE_MAX_LENGTH,
        choices=PLANT_TYPE_CHOICES,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                    r'^[a-zA-Z]+$',
                    message="Plant name should contain only letters!"
                )
            ]
    )
    image_url = models.URLField(
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False
    )
