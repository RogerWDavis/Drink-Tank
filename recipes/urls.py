from django.urls import path
from .views import (
    AddRecipe, Recipes,
    RecipeDetail, DeleteRecipe,
    EditRecipe, HomeView
)

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", HomeView.as_view(), name="home"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe",),
    path('accounts/', include('allauth.urls')),
]
