from random import choice

from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage

from .forms import RecipeAddForm
from .models import Recipe


def recipe_add_form(request):
    if not request.user.is_authenticated:
        text = 'Сначала нужно войти в систему перед тем, как добавлять рецепты'
        return render(request, 'base.html', {'text': text})
    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']
            ingredients = form.cleaned_data['ingredients']
            recipe = Recipe(name=name, description=description, cooking_steps=cooking_steps, cooking_time=cooking_time,
                            image=image, ingredients=ingredients, rating=9.99, author=request.user)
            recipe.save()

            fs = FileSystemStorage()
            fs.save(image.name, image)

            return render(request, 'base.html', {'text': 'Успешно отправлено'})
    else:
        form = RecipeAddForm()
    return render(request, 'recipeapp/recipe_add_form.html', {'form': form})


def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user.id != recipe.author.id:
        text = 'Вы не авторизованы для редактирования этого рецепта'
        return render(request, 'base.html', {'text': text})
    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            recipe.name = form.cleaned_data['name']
            recipe.description = form.cleaned_data['description']
            recipe.cooking_steps = form.cleaned_data['cooking_steps']
            recipe.cooking_time = form.cleaned_data['cooking_time']
            recipe.image = form.cleaned_data['image']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.save()

            fs = FileSystemStorage()
            fs.save(recipe.image.name, recipe.image)

            return render(request, 'base.html', {'text': 'Успешно отправлено'})
    else:
        form = RecipeAddForm()
    return render(request, 'recipeapp/recipe_add_form.html', {'form': form})


def show_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipeapp/show_recipe.html', {'recipe': recipe})


def show_random_recipes(request):
    recipes_ids = list(Recipe.objects.values_list("id", flat=True))
    if not recipes_ids:
        text = 'В базе данных нет ни одного рецепта. Нужно добавить рецепты.'
        return render(request, 'base.html', {'text': text})
    recipes = []
    for i in range(5):
        recipe = get_object_or_404(Recipe, pk=choice(recipes_ids))
        recipes.append(recipe)
    return render(request, 'recipeapp/index.html', {'recipes': recipes})

