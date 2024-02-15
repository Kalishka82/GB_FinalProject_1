from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = []


def index(request):
    """Отображает страницу-приветствие проекта"""
    return HttpResponse('<h1>Вот он я - ПОВАРЁНОК - мой новый сайт с рецептами вкусняшек для меня и моих друзей.</h1>')
    # return render(request, template_name='index.html')


def recipes(request):
    return HttpResponse(f'<h1>Рецепты</h1>')


def recipe_by_id(request, recipe_id):
    return HttpResponse(f'<h1>Рецепты</h1><p>{recipe_id}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
