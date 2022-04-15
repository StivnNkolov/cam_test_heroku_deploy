from decimal import Decimal

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from cam_0504.main_content.filters import RecipeFilter
from cam_0504.main_content.forms import RecipeCreateForm, RecipeDeleteForm, RecipePriceIncreasePercentUpdateForm, \
    IngredientCreateForm
from cam_0504.main_content.models import Recipe, IncreasePercentage, Ingredient
from common.calculations import calculate_price
from common.mixins import AuthenticationRedirectToLoginMixin


class RecipesListView(AuthenticationRedirectToLoginMixin, generic_views.ListView):
    template_name = 'main_content/all_recipes.html'
    model = Recipe

    def get_queryset(self):
        needed_queryset = Recipe.objects.filter(user=self.request.user)
        return needed_queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_filter = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        context['object_list'] = recipe_filter.qs
        context['recipe_filter'] = recipe_filter
        return context


class RecipeCreateView(AuthenticationRedirectToLoginMixin, generic_views.CreateView):
    template_name = 'main_content/recipe_create.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class RecipeDetailsView(AuthenticationRedirectToLoginMixin, generic_views.DetailView):
    template_name = 'main_content/recipe_details.html'
    model = Recipe


class RecipeDeleteView(AuthenticationRedirectToLoginMixin, generic_views.DeleteView):
    template_name = 'main_content/recipe_delete.html'
    model = Recipe
    form_class = RecipeDeleteForm
    success_url = reverse_lazy('recipes list')


def recipe_finalise(request, pk):
    recipe = Recipe.objects.prefetch_related('recipeingredient_set').get(id=pk)
    ingredients = recipe.recipeingredient_set.all()
    recipe_increase_percentage = recipe.increasepercentage.percentage
    price, increased_price = calculate_price(recipe_increase_percentage, ingredients)
    recipe.price = price
    recipe.increased_price = increased_price
    recipe.save()
    return redirect('recipe details', pk)


class RecipePriceIncreasePercentUpdate(AuthenticationRedirectToLoginMixin, generic_views.UpdateView):
    template_name = 'main_content/recipe_price__increase_percentage_create.html'
    model = IncreasePercentage
    form_class = RecipePriceIncreasePercentUpdateForm

    def get_success_url(self):
        percentage = IncreasePercentage.objects.get(id=self.kwargs['pk'])
        recipe_percentage_id = percentage.recipe.id
        return reverse_lazy('recipe details', kwargs={'pk': recipe_percentage_id})


class RecipeAddAsIngredientView(AuthenticationRedirectToLoginMixin, generic_views.CreateView):
    template_name = 'main_content/recipe_add_as_ingredient.html'
    model = Ingredient
    form_class = IngredientCreateForm

    def get_form(self, form_class=None):
        form = super().get_form(self.form_class)
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        form.initial = {
            'name': recipe.name,
            'price_per_type': Decimal(recipe.price),
        }
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
