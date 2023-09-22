from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

@admin.register(models.Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    summer_fields = ('content')




