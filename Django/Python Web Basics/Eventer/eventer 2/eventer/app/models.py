from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MinLengthValidator

# DOUBLE CHECK IF REQUIRED IS NEEDED


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


def validate_password_contains_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit!")


def validate_date_not_in_past(value):
    if value < date.today():
        raise ValidationError("The date cannot be in the past!")


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=20,
        validators=[validate_only_letters])
    last_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(4)])
    email = models.EmailField(
        max_length=45)
    profile_picture = models.URLField(
        blank=True,
        null=True)
    password = models.CharField(
        max_length=20,
        validators=[validate_password_contains_digit, MinLengthValidator(5)])


class EventModel(models.Model):
    CATEGORY_CHOICES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    event_name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2)])
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES)
    description = models.TextField(
        blank=True,
        null=True)
    date = models.DateField(
        validators=[validate_date_not_in_past])
    event_image = models.URLField()
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
