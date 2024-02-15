from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddRecipeForm(forms.ModelForm):
    """ Форма добавления рецепта. """

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_time']


class RegisterUserForm(UserCreationForm):
    """ Форма регистрации пользователя. """
    login = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('login', 'name', 'surname', 'phone', 'password1', 'password2')
