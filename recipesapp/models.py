from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipesimg/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categoriesimg')

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
