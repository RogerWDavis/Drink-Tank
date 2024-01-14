from allauth.account.views import LoginView as BaseLoginView
from django.contrib.auth.forms import UserCreationForm
from allauth.account.views import SignupView
from .forms import CustomSignupForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)

from .models import Profile
from recipes.models import Recipe
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

class Profiles(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        user_id = self.kwargs["pk"]
        profile = get_object_or_404(Profile, user__id=user_id)
        user_recipes = Recipe.objects.filter(author=profile.user)

        context = {
            "profile": profile,
            "form": ProfileForm(instance=profile),
            "user_recipes": user_recipes,
        }
        return context

class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    form_class = ProfileForm
    model = Profile
    template_name = 'editprofile.html'
    
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class LoginView(BaseLoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

class LogoutView(BaseLogoutView):
    template_name = 'logout.html'


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'signup.html'

    def after_signup(self, form):
        response = super().after_signup(form)
        user = form.save(self.request)
        user_id = user.pk if user is not None else None

        if user_id:
            # Save the profile picture to the user's profile
            profile = user.profile
            profile.image = form.cleaned_data['profile_picture']
            profile.save()

            return redirect(reverse_lazy('profile', kwargs={'pk': user_id}))
        else:
            return response

    def get_success_url(self):
        if hasattr(self, 'user') and self.user is not None:
            user_id = self.user.pk
            return reverse_lazy('profile', kwargs={'pk': user_id})
        else:
            return super().get_success_url()

    

class HomeView(TemplateView):
    template_name = 'home.html'
