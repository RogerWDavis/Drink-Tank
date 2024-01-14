from allauth.account.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import (
    american_whiskey_article,
    irish_whiskey_article,
    japanese_whiskey_article,
    scotch_whiskey_article,
    AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe,
)
from user.views import HomeView, Profiles, EditProfile, CustomSignupView, LoginView, LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="editprofile"),
    path('accounts/', include('allauth.urls')),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path("american-whiskey/", american_whiskey_article, name='awhiskey'),
    path("irish-whiskey/", irish_whiskey_article, name='iwhiskey'),
    path("japanese-whiskey/", japanese_whiskey_article, name='jwhiskey'),
    path("scotch-whiskey/", scotch_whiskey_article, name='swhiskey'),
    path("add-recipe/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("recipes/<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("recipes/delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("recipes/edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
