from django import forms
from allauth.account.forms import SignupForm
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["username", "bio", 'image']

        labels = {"username": "Name", "bio": "Bio"}


class CustomSignupForm(SignupForm):
    profile_picture = forms.ImageField(label='Profile Picture', required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.profile.image = self.cleaned_data['profile_picture']
        user.profile.save()

        return user