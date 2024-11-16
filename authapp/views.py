from django.shortcuts import render
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def registration_view(request):
    if request.user.is_authenticated:
        text = 'Сначала нужно выйти из системы, чтобы зарегистрировать нового пользователя'
        return render(request, 'base.html', {'text': text})
    if request.method == 'POST':
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            text = f'Вы зарегистрировались как {user}'
            return render(request, 'base.html', {'text': text})
    else:
        form = BaseUserCreationForm()
    message = 'Регистрация нового пользователя'
    return render(request, 'authapp/auth_form.html', {'form': form, 'message': message})


def login_view(request):
    if request.user.is_authenticated:
        text = 'Вы уже в системе. Сначала нужно выйти из нее, чтобы зайти под другим логином'
        return render(request, 'base.html', {'text': text})
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            text = f'Вы вошли в систему как {user}'
            return render(request, 'base.html', {'text': text})
    else:
        form = AuthenticationForm()
    message = 'Вход для зарегистрированных пользователей'
    return render(request, 'authapp/auth_form.html', {'form': form, 'message': message})


def logout_view(request):
    logout(request)
    text = 'Вы вышли из системы'
    return render(request, 'base.html', {'text': text})
