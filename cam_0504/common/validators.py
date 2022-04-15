import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ONLY_LETTERS_VALIDATION_ERROR_MESSAGE = 'The value must consist of only letters!'
LETTERS_AND_NUMBERS_VALIDATION_ERROR_MESSAGE = 'The value must consist of only letters and numbers!'


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError(ONLY_LETTERS_VALIDATION_ERROR_MESSAGE)


def letters_and_numbers_validator(value):
    if not value.isalnum():
        raise ValidationError(LETTERS_AND_NUMBERS_VALIDATION_ERROR_MESSAGE)


# TODO refactor this make it more abstract. RegexValidator
@deconstructible
class LettersNumbersWhitespacesValidator:
    def __init__(self, regex_pattern):
        self.regex_pattern = regex_pattern

    def __call__(self, value):
        if not re.match(self.regex_pattern, value):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __get_exception_message():
        return 'Name can consist of letters, whitespaces and numbers. "Tomato soup"'
