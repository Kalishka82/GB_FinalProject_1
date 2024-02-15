from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import *
from .models import *

menu = [{'title': 'Вкусняшки', 'url': 'all_recipes'},
        {'title': 'Добавить вкусняшку', 'url': 'add_recipe'}]


def index(request):
    """Отображает страницу-приветствие проекта"""
    context = {'menu': menu, 'title': 'ПОВАРЁНОК'}

    return render(request, 'myapp/index.html', context)


def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'menu': menu, 'title': 'ВКУСНЯШКИ', 'recipes': recipes}

    return render(request, 'myapp/recipe_list.html', context)


def recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = IngredientInRecipe.objects.filter(recipe_id=recipe_id)
    context = {'menu': menu, 'title': {recipe_id}, 'recipe': recipe, 'ingredients': ingredients}

    return render(request, 'myapp/recipe.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления вкусняшки')
    else:
        form = AddRecipeForm()
    context = {'menu': menu, 'title': 'Добавление вкусняшки', 'form': form}

    return render(request, 'myapp/addrecipe.html', context)


def register(request):
    return HttpResponse(f'<h1>Регистрация</h1>')


def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
