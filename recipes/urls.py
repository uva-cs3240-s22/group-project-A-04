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
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),

    # All-Auth Views
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

