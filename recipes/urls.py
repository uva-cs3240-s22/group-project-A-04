# recipes/urls.py
#
# url views for recipes app


# Imports from Django library
from django.urls import path

# Importing views from current directory
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeIndex.as_view(), name='index'),
    path('create/', views.recipe_create_view, name="create"),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='detail'),
    path('<int:pk>/fork/', views.recipe_fork_view, name='fork'),
    path('<int:pk>/edit/', views.recipe_update_view, name='edit'),
    path('<int:pk>/delete/', views.RecipeDelete.as_view(), name='delete'),
    path('<int:pk>/recipe_like/', views.recipe_like, name='recipe_like'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search/', views.SearchResults.as_view(), name='SearchResults'),
]

