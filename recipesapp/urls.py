from django.urls import path
from .views import recipe_add_form, show_random_recipes, show_recipe, update_recipe

urlpatterns = [
    path('new-recipe/', recipe_add_form, name='recipe_add_form'),
    path('', show_random_recipes, name='show_random_recipes'),
    path('recipe/<int:recipe_id>', show_recipe, name='show_recipe'),
    path('update-recipe/<int:recipe_id>', update_recipe, name='update_recipe'),
]
