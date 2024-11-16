from django import forms
from .models import Recipe


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'image', 'ingredients']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'cooking_steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (минуты)',
            'image': 'Изображение',
            'ingredients': 'Ингредиенты',
        }


# class UserForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.TextField()
#     cooking_steps = forms.TextField()
#     cooking_time = forms.IntegerField()
#     image = forms.ImageField(upload_to='recipesimg/')
#     author = forms.ForeignKey(User, on_delete=models.CASCADE)
#     ingredients = forms.TextField()
#     rating = forms.DecimalField(max_digits=3, decimal_places=2)
#     create_date = forms.DateTimeField(auto_now_add=True)
