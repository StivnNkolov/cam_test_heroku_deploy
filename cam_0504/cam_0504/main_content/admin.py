from django.contrib import admin

from cam_0504.main_content.models import Ingredient, Recipe, RecipeIngredient, IncreasePercentage


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(IncreasePercentage)
class IncreasePercentageAdmin(admin.ModelAdmin):
    pass
