from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='')
    ingredients = models.TextField(max_length=250, default='')
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Recipe")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
