from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Recipe
from .forms import RecipeForm

class Recipes(ListView):

    template_name = "index.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return self.model.objects.all()

class RecipeDetail(DetailView):

    template_name = "recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"

class AddRecipe(LoginRequiredMixin, CreateView):

    template_name = "add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
 
    template_name = 'redit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'
    
    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user
