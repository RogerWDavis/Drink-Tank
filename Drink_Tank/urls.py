from django.contrib import admin
from django.urls import path, include
from recipes.views import (
    AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe,
)
from user.views import (Profiles, EditProfile,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Recipes.as_view(), name='recipes'),
    path('auth/', include('auth.urls')),
    path('auth/', include('allauth.urls')),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit-profile/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),

]
