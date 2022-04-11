# Imports from Django library
from django.urls import path

# Importing views from current directory
from . import views

app_name = 's3'

urlpatterns = [
    path('', views.RecipeIndex.as_view(), name='index'),
]