from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from common.validators import LettersNumbersWhitespacesValidator

UserModel = get_user_model()


class Ingredient(models.Model):
    REGEX_PATTERN = '(?<![\s\W\D])^([a-zA-Zа-яА-Я0-9]+[\s]?[a-zA-Zа-яА-Я0-9]+)+$(?![\s\W\D])'

    NAME_MAX_LEN = 30
    NAME_VERBOSE_NAME = 'Name'
    NAME_MIN_LENGTH_VALUE = 2

    TYPE_CHOICES = ['Kilogram', 'Liter', 'Piece']
    TYPE_DEFAULT_VALUE = 'Kilogram'
    TYPE_VERBOSE_NAME = 'For'

    PRICE_PER_TYPE_MD = 6
    PRICE_PER_TYPE_DP = 3
    PRICE_PER_TYPE_VERBOSE_NAME = 'Price in leva'
    PRICE_PER_TYPE_MIN_VALUE = 0

    CALCULATED_PRICE_MD = 6
    CALCULATED_PRICE_DP = 3

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        verbose_name=NAME_VERBOSE_NAME,
        validators=[
            LettersNumbersWhitespacesValidator(REGEX_PATTERN),
            MinLengthValidator(NAME_MIN_LENGTH_VALUE),
        ],
    )

    type = models.CharField(
        max_length=max([len(el) for el in TYPE_CHOICES]),
        choices=((el, el) for el in TYPE_CHOICES),
        default=TYPE_DEFAULT_VALUE,
        verbose_name=TYPE_VERBOSE_NAME,
    )

    price_per_type = models.DecimalField(
        max_digits=PRICE_PER_TYPE_MD,
        decimal_places=PRICE_PER_TYPE_DP,
        verbose_name=PRICE_PER_TYPE_VERBOSE_NAME,
        validators=[
            MinValueValidator(PRICE_PER_TYPE_MIN_VALUE),
        ],
    )

    date_created = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='user_ingredient_name_unique')
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    NAME_MAX_LENGTH = 120
    NAME_VERBOSE_NAME = 'Recipe name'
    NAME_MIN_LENGTH = 2

    PRICE_DEFAULT_VALUE = 0
    PRICE_MD = 6
    PRICE_DP = 3

    REGEX_PATTERN = '(?<![\s\W\D])^([a-zA-Zа-яА-Я0-9]+[\s]?[a-zA-Zа-яА-Я0-9]+)+$(?![\s\W\D])'

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name=NAME_VERBOSE_NAME,
        validators=[
            LettersNumbersWhitespacesValidator(REGEX_PATTERN),
            MinLengthValidator(NAME_MIN_LENGTH),
        ],

    )

    price = models.DecimalField(
        max_digits=PRICE_MD,
        decimal_places=PRICE_DP,
        default=PRICE_DEFAULT_VALUE,
        null=True,
        blank=True,

    )

    increased_price = models.DecimalField(
        max_digits=PRICE_MD,
        decimal_places=PRICE_DP,
        default=PRICE_DEFAULT_VALUE,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='user_recipe_name_unique')
        ]

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    AMOUNT_VERBOSE_NAME = 'Quantity in grams / pieces'
    AMOUNT_DEFAULT_VALUE = 0
    AMOUNT_MD = 6
    AMOUNT_DP = 2
    AMOUNT_MIN_VALUE = 1

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        verbose_name=AMOUNT_VERBOSE_NAME,
        max_digits=AMOUNT_MD,
        decimal_places=AMOUNT_DP,
        default=AMOUNT_DEFAULT_VALUE,
        validators=[
            MinValueValidator(AMOUNT_MIN_VALUE),
        ],
    )

    def __str__(self):
        return self.ingredient.name


class IncreasePercentage(models.Model):
    PERCENTAGE_MIN_VALUE = 1
    PERCENTAGE_DEFAULT_VALUE = 0

    recipe = models.OneToOneField(
        Recipe,
        on_delete=models.CASCADE,
    )

    percentage = models.IntegerField(
        default=PERCENTAGE_DEFAULT_VALUE,
        validators=[
            MinValueValidator(PERCENTAGE_MIN_VALUE),
        ]

    )

    def __str__(self):
        return f'{self.percentage} percent increase for {self.recipe}'
