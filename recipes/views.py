from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

class Recipes(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'

class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes_detail.html'
    context_object_name = 'recipe'

class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk}) 

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk}) 

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('recipes')

    def test_func(self):
        return self.request.user == self.get_object().author

def american_whiskey_article(request):
    return render(request, 'awhiskey.html')

def irish_whiskey_article(request):
    return render(request, 'iwhiskey.html')

def japanese_whiskey_article(request):
    return render(request, 'jwhiskey.html')

def scotch_whiskey_article(request):
    return render(request, 'swhiskey.html')
