from django.urls import path
from .views import (
    LoginView, LogoutView, AlreadyLoggedInView,
    SetPasswordView, SignupView, LoggedInView,
    LoggedOutView, PasswordChangedView, PasswordSetView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('already-logged-in/', AlreadyLoggedInView.as_view(), name='already-logged-in'),
    path('set-password/', SetPasswordView.as_view(), name='set-password'),
    path('signup/', SignupView.as_view(), name='user-signup'),
    path('logged-in/', LoggedInView.as_view(), name='user-logged-in'),
    path('logged-out/', LoggedOutView.as_view(), name='user-logged-out'),
    path('password-changed/', PasswordChangedView.as_view(), name='password-changed'),
    path('password-set/', PasswordSetView.as_view(), name='password-set'),
]

