from django.urls import path

from cam_0504.main_content.views.generic import HomeView
from cam_0504.main_content.views.ingredient import IngredientsListView, IngredientCreateView, IngredientEditView, \
    IngredientDeleteView
from cam_0504.main_content.views.recipe import RecipesListView, RecipeCreateView, RecipeDetailsView, recipe_finalise, \
    RecipeDeleteView, RecipePriceIncreasePercentUpdate, RecipeAddAsIngredientView
from cam_0504.main_content.views.recipe_ingredient import RecipeIngredientCreateView, RecipeIngredientEditView, \
    recipe_ingredient_delete_view

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('ingredients/', IngredientsListView.as_view(), name='ingredients list'),
    path('ingredient/create/', IngredientCreateView.as_view(), name='ingredient create'),
    path('ingredient/edit/<int:pk>/', IngredientEditView.as_view(), name='ingredient edit'),
    path('ingredient/delete/<int:pk>/', IngredientDeleteView.as_view(), name='ingredient delete'),

    path('recipes/', RecipesListView.as_view(), name='recipes list'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe create'),
    path('recipe/details/<int:pk>/', RecipeDetailsView.as_view(), name='recipe details'),
    path('recipe/finalise/<int:pk>/', recipe_finalise, name='recipe finalise'),
    path('recipe/delete/<int:pk>', RecipeDeleteView.as_view(), name='recipe delete'),
    path('recipe/price_increase/<int:pk>/', RecipePriceIncreasePercentUpdate.as_view(),
         name='recipe increase price percentage'),
    path('recipe/as_ingredient/<int:pk>/', RecipeAddAsIngredientView.as_view(), name='recipe add as ingredient'),

    path('recipe_ingredient/create/<int:pk>', RecipeIngredientCreateView.as_view(), name='recipe ingredient create'),
    path('recipe_ingredient/edit/<int:pk>/', RecipeIngredientEditView.as_view(), name='recipe ingredient edit'),
    path('recipe_ingredient/delete/<int:pk>/', recipe_ingredient_delete_view, name='recipe ingredient delete'),

]
