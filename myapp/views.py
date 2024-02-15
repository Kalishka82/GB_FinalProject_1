from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'Рецепты', 'url': 'all_recipes'},
        {'title': 'Добавить рецепт', 'url': 'add_recipe'}]


def index(request):
    """Отображает страницу-приветствие проекта"""
    context = {'menu': menu, 'title': 'ПОВАРЁНОК'}

    return render(request, 'myapp/index.html', context)


def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'menu': menu, 'title': 'ПОВАРЁНОК', 'recipes': recipes}

    return render(request, 'myapp/recipe_list.html', context)


def recipe_by_id(request, recipe_id):
    return HttpResponse(f'<h1>Рецепты</h1><p>{recipe_id}</p>')


def add_recipe(request):
    return HttpResponse(f'<h1>Добавить рецепт</h1>')


def register(request):
    return HttpResponse(f'<h1>Регистрация</h1>')


def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
