from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('recipes/', all_recipes, name='all_recipes'),  # http://127.0.0.1:8000/recipes/
    path('recipes/<int:recipe_id>/', recipe_by_id, name='recipe_by_id'),  # http://127.0.0.1:8000/recipes/recipe_id/
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('addrecipe', add_recipe, name='add_recipe')
]
