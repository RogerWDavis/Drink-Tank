from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(TemplateView):
    template_name = 'account/login.html'

class LogoutView(TemplateView):
    template_name = 'account/logout.html'

class AlreadyLoggedInView(TemplateView):
    template_name = 'account/already_logged_in.html'

class SetPasswordView(LoginRequiredMixin, TemplateView):
    template_name = 'account/set_password.html'

class SignupView(TemplateView):
    template_name = 'account/signup.html'

class LoggedInView(TemplateView):
    template_name = 'account/loggedin.txt'

class LoggedOutView(TemplateView):
    template_name = 'account/loggedout.txt'

class PasswordChangedView(TemplateView):
    template_name = 'account/passchanged.txt'

class PasswordSetView(TemplateView):
    template_name = 'account/passset.txt'

