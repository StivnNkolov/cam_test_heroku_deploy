from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from cam_0504.main_content.models import Ingredient, Recipe, IncreasePercentage, RecipeIngredient


class IngredientCreateForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    # TODO research
    def save(self, commit=True):
        current_ingredient = super().save(commit=False)
        current_ingredient.user = self.user

        if commit:
            current_ingredient.save()
        return current_ingredient

    class Meta:
        model = Ingredient
        fields = ['name', 'price_per_type', 'type']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Cucumber/Rice',
                },
            ),
            'price_per_type': forms.NumberInput(
                attrs={
                    'placeholder': '2.50/3.85',
                    'min': 0,
                },
            ),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'TEST ERROR MESSAGE',
            },
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        try:
            Ingredient.objects.get(user=self.user, name=cleaned_data['name'])
        except Ingredient.DoesNotExist:
            pass
        else:
            raise ValidationError('Ingredient with that name already exist')

        return cleaned_data


class IngredientEditForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price_per_type', 'type']
        widgets = {
            'price_per_type': forms.NumberInput(
                attrs={
                    'min': 0,
                }
            )
        }


class IngredientDeleteForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = []


class RecipeCreateForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        current_recipe = super().save(commit=False)
        current_recipe.user = self.user

        if commit:
            current_recipe.save()
            increase_percentage = IncreasePercentage.objects.create(
                recipe=current_recipe,
            )
        return current_recipe

    class Meta:
        model = Recipe
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Hoso Tuna/Bread',
                },
            ),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        try:
            Recipe.objects.get(user=self.user, name=cleaned_data['name'])
        except Recipe.DoesNotExist:
            pass
        else:
            raise ValidationError('Recipe with that name already exist')

        return cleaned_data


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = []


class RecipePriceIncreasePercentUpdateForm(forms.ModelForm):
    class Meta:
        model = IncreasePercentage
        fields = ['percentage']
        widgets = {
            'percentage': forms.NumberInput(
                attrs={
                    'min': 0,
                },
            ),
        }


class RecipeIngredientCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'amount']
        labels = {
            'ingredient': 'Съставка',
        }
        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'min': 0,
                },
            ),
        }


class RecipeIngredientEditForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(
                attrs={
                    'min': 0,
                },
            ),
        }
