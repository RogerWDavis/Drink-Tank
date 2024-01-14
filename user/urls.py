from django.urls import path
from .views import HomeView, Profiles, EditProfile, CustomSignupView, LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="editprofile"),
    path('accounts/', include('allauth.urls')),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('changepass/', PasswordChangeView.as_view(), name='changepass'),
    path('setpass/', PasswordResetView.as_view(), name='setpass'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
