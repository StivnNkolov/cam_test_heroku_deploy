from cam_0504.main_content.models import Recipe, Ingredient


def get_user_recipes_ingredients_count(user):
    recipes = Recipe.objects.filter(user=user).count()
    ingredients = Ingredient.objects.filter(user=user).count()

    return recipes, ingredients
