from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField(max_length=250, default='')
    content = models.TextField()
    image = models.ImageField(upload_to='ad_pictures', default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Recipe")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)