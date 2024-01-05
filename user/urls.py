from django.urls import path
from .views import Profiles, EditProfile, SignUpView, LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('changepass/', PasswordChangeView.as_view(), name='changepass'),
    path('setpass/', PasswordResetView.as_view(), name='setpass'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]