from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from recipes.views import (
    AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe, HomeView
)
from user.views import (Profiles, EditProfile, SignUpView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(template_name='signup.html'), name='signup'),
    path("recipes/<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"), 
    path("recipes/add/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),  
    path("recipes/edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),  
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit-profile/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),
]
