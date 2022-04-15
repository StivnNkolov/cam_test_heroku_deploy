from django.urls import reverse_lazy
from django.views import generic as generic_views

from cam_0504.main_content.filters import IngredientFilter
from cam_0504.main_content.forms import IngredientCreateForm, IngredientEditForm, IngredientDeleteForm
from cam_0504.main_content.models import Ingredient
from common.mixins import AuthenticationRedirectToLoginMixin


class IngredientsListView(AuthenticationRedirectToLoginMixin, generic_views.ListView):
    template_name = 'main_content/all_ingredients.html'
    model = Ingredient

    def get_queryset(self):
        needed_queryset = Ingredient.objects.filter(user=self.request.user)
        return needed_queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_filter = IngredientFilter(self.request.GET, queryset=self.get_queryset())
        context['object_list'] = ingredient_filter.qs
        context['ingredient_filter'] = ingredient_filter
        return context


class IngredientCreateView(AuthenticationRedirectToLoginMixin, generic_views.CreateView):
    template_name = 'main_content/ingredient_create.html'
    model = Ingredient
    form_class = IngredientCreateForm
    success_url = reverse_lazy('ingredients list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class IngredientEditView(AuthenticationRedirectToLoginMixin, generic_views.UpdateView):
    template_name = 'main_content/ingredient_edit.html'
    model = Ingredient
    form_class = IngredientEditForm
    success_url = reverse_lazy('ingredients list')


class IngredientDeleteView(AuthenticationRedirectToLoginMixin, generic_views.DeleteView):
    template_name = 'main_content/ingredient_delete.html'
    model = Ingredient
    form_class = IngredientDeleteForm
    success_url = reverse_lazy('ingredients list')
