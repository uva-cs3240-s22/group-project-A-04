# recipes/urls.py
#
# url views for recipes app


# Imports from Django library
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

# Importing views from current directory
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeIndex.as_view(), name='index'),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', views.RecipeModify.as_view(), name='edit'),
    path('create/', views.recipe_create_view, name="create"),
]

