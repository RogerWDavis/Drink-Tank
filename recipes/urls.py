from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipe.as_view(), name="home"),
]
