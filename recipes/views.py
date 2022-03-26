# recipes/views.py
# 
# views for the recipe app

# Imports from Django library
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

# Importing models from current directory
from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/details.html'


class EditView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/edit.html'

