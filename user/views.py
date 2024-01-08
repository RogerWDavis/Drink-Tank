
from allauth.account.views import LoginView as BaseLoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
    PasswordChangeView as BasePasswordChangeView,
    PasswordResetView as BasePasswordResetView,
    PasswordResetConfirmView as BasePasswordResetConfirmView,
)

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse


from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Profile

class Profiles(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        user_id = self.kwargs["pk"]
        profile = get_object_or_404(Profile, user__id=user_id)
        context = {
            "profile": profile,
            'form': ProfileForm(instance=profile)
        }
        return context



class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)

        
        return response


class LoginView(BaseLoginView):
    template_name = 'login.html'

    def get_success_url(self):
    
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class LogoutView(BaseLogoutView):
    template_name = 'logout.html'


class PasswordChangeView(BasePasswordChangeView):
    template_name = 'changepass.html'
    success_url = reverse_lazy('password_change_done')


class PasswordResetView(BasePasswordResetView):
    template_name = 'setpass.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')