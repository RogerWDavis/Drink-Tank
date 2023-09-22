from django.shortcuts import render
from django.views import generic
from .models import Recipe
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class recipe(generic.ListView):

    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


