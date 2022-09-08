from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main.validators import only_letters_validator

# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH=2
    LAST_NAME_MIN_LENGTH=2    
    FIRST_NAME_MAX_LENGTH=30
    LAST_NAME_MAX_LENGTH=30

    MALE="Male"
    FEMALE="Female"
    DO_NOT_SHOW="Do not show"

    GENDERS=[(x,x) for x in (MALE,FEMALE,DO_NOT_SHOW)]


    #id/pk by default
    first_name=models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )
    first_name=models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )
    picture=models.URLField()

    date_of_birth=models.DateField(
        null=True,
        blank=True
    )
    description=models.TextField(
        null=True,
        blank=True,
    )
    gender=models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

class Pet(models.Model):
    CAT="Cat"
    DOG="Dog"
    BUNNY="Bunny"
    PARROT="Parrot"
    FISH="Fish"
    OTHER="Other"

    TYPES=((x,x) for x in (CAT,DOG,BUNNY,PARROT,FISH,OTHER))
    NAME_MAX_LENGTH=30

    name=models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type=models.CharField(
        max_length=max(len(x) for(x,_)in TYPES)
    )

    date_of_birth=models.DateField(
        null=True, 
        blank=True
    )

    user_profile=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together=("user_profile","name")


class PetPhoto(models.Model):
    photo=models.ImageField(
        validators=(
            #validate_file_max_size_in_mb(5)
        )
    )
    tagged_pets=models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True, 
        blank=True
    )

    publication_date=models.DateTimeField(
        auto_now_add=True,
    
    )

    likes=models.IntegerField(
        default=0
    )