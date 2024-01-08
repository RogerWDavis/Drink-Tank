
from django.urls import path
from .views import (
    AddRecipe, Recipes,
    RecipeDetail, DeleteRecipe,
    EditRecipe, HomeView
)

from .views import (
    american_whiskey_article,
    irish_whiskey_article,
    japanese_whiskey_article,
    scotch_whiskey_article,
)

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", HomeView.as_view(), name="home"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("recipes/<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"), 
    path("recipes/delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),  
    path("recipes/edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path('american-whiskey/', american_whiskey_article, name='awhiskey'),
    path('irish-whiskey/', irish_whiskey_article, name='iwhiskey'),
    path('japanese-whiskey/', japanese_whiskey_article, name='jwhiskey'),
    path('scotch-whiskey/', scotch_whiskey_article, name='swhiskey'),
]
