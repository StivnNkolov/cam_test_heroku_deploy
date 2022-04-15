from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from cam_0504.main_content.forms import RecipeIngredientCreateForm, RecipeIngredientEditForm
from cam_0504.main_content.models import RecipeIngredient, Recipe, Ingredient
from common.mixins import AuthenticationRedirectToLoginMixin


class RecipeIngredientCreateView(AuthenticationRedirectToLoginMixin, generic_views.CreateView):
    template_name = 'main_content/recipe_ingredient_create.html'
    model = RecipeIngredient
    form_class = RecipeIngredientCreateForm

    success_url = reverse_lazy('recipe details')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        context['recipe'] = recipe
        return context

    def form_valid(self, form):
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        recipe_ingredient = RecipeIngredient.objects.create(
            recipe=recipe,
            ingredient=form.cleaned_data['ingredient'],
            amount=form.cleaned_data['amount'],
        )
        recipe_ingredient.save()
        return redirect('recipe details', self.kwargs['pk'])

    # TODO not sure if this is the way!
    def get_queryset(self):
        queryset = Ingredient.objects.filter(user=self.request.user)
        return queryset

    def get_form(self, form_class=None):
        form = super(RecipeIngredientCreateView, self).get_form(self.form_class)
        choices = self.get_queryset()
        form.fields['ingredient'].queryset = choices
        return form


class RecipeIngredientEditView(AuthenticationRedirectToLoginMixin, generic_views.UpdateView):
    template_name = 'main_content/recipe_ingr_edit.html'
    model = RecipeIngredient
    form_class = RecipeIngredientEditForm

    def get_success_url(self):
        recipe_id = Recipe.objects.get(recipeingredient=self.object).id
        return reverse_lazy('recipe details', kwargs={'pk': recipe_id})


def recipe_ingredient_delete_view(request, pk):
    recipe_ingredient = RecipeIngredient.objects.get(id=pk)
    recipe = recipe_ingredient.recipe
    recipe_ingredient.delete()
    return redirect('recipe details', recipe.id)
