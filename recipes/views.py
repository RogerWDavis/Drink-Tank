from django.views.generic import TemplateView
from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy

class Recipes(ListView):

    template_name = "recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return self.model.objects.all()

class RecipeDetail(DetailView):

    template_name = "recipes_detail.html"
    model = Recipe
    context_object_name = "recipe"

class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    fields = ['title', 'ingredients', 'content', 'image']
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
 
    template_name = 'edit_recipe.html'
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

class HomeView(TemplateView):
   
    template_name = 'home.html'


def american_whiskey_article(request):
     return render(request, 'awhiskey.html', {'whiskey_type': 'american'})

def irish_whiskey_article(request):
    return render(request, 'iwhiskey.html', {'whiskey_type': 'irish'}  )

def japanese_whiskey_article(request):
    return render(request, 'jwhiskey.html', {'whiskey_type': 'japanese'} )

def scotch_whiskey_article(request):
    return render(request, 'swhiskey.html', {'whiskey_type': 'scotch'} )