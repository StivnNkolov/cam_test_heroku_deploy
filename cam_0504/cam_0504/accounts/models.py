from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cam_0504.accounts.managers import AppUserManager
from common.validators import only_letters_validator, LettersNumbersWhitespacesValidator


# TODO make more abstract the LEttersNUmbers validator.!!

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 72
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_VERBOSE_NAME = 'First Name'
    FIRST_NAME_HELP_TEXT = 'Enter your first name'

    LAST_NAME_MAX_LEN = 72
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_VERBOSE_NAME = 'Last Name'
    LAST_NAME_HELP_TEXT = 'Enter your last name'

    CITY_NAME_MAX_LEN = 72
    CITY_NAME_MIN_LEN = 2
    CITY_VERBOSE_NAME = 'City'
    CITY_HELP_TEXT = "Enter your city's name"

    AGE_MIN_VALUE = 0
    AGE_VERBOSE_NAME = 'Age'
    AGE_HELP_TEXT = 'Enter your age'

    RESTAURANT_NAME_MAX_LEN = 100
    RESTAURANT_NAME_MIN_LEN = 1
    RESTAURANT_VERBOSE_NAME = "Restaurant's name"
    RESTAURANT_HELP_TEXT = 'Enter the name of your restaurant'

    REGEX_PATTERN = '(?<![\s\W\D])^([a-zA-Z0-9]+[\s]?[a-zA-Z0-9]+)+$(?![\s\W\D])'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name=FIRST_NAME_VERBOSE_NAME,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,
        ]
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name=LAST_NAME_VERBOSE_NAME,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        ]
    )
    city_name = models.CharField(
        max_length=CITY_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name=CITY_VERBOSE_NAME,
        validators=[

            only_letters_validator,
            MinLengthValidator(CITY_NAME_MIN_LEN)
        ]
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=AGE_VERBOSE_NAME,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ]
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    restaurant_name = models.CharField(
        max_length=RESTAURANT_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name=RESTAURANT_VERBOSE_NAME,
        validators=[
            LettersNumbersWhitespacesValidator(REGEX_PATTERN),
            MinLengthValidator(RESTAURANT_NAME_MIN_LEN),
        ]
    )
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.email
