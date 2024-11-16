from django.contrib import admin
from .models import Recipe, Category, RecipeCategory


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'rating', 'create_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'recipe', 'is_liked', 'is_hidden']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
