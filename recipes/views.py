from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('<h1>Welcome to the Recipes home page</h1>')

