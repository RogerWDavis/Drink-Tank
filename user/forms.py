from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["username", "bio"]

        labels = {"username": "Name", "bio": "Bio"}