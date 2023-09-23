from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            "title",
            "content",
            "ingredients",
        ]

        ingredients = forms.CharField()

        widget = {
            "content": forms.Textarea(),
        }

        labels = {
            "title": "Recipe Title",
            "content": "Content",
            "ingredients": "Recipe Ingredients",
        }