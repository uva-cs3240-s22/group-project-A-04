# recipes/views.py
# 
# views for the recipe app

# Imports from Django library
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Importing models from current directory
from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Recipe.objects


class EditView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/edit.html'

class FormView(generic.CreateView):
    model = Recipe
    template_name = 'recipes/form.html'
    fields = ["recipe_name", "description", "procedure","author"]
    def get_success_url(self):
        return reverse('recipes:index')
    # initial = {"pub_date": str(timezone.now()), "mod_date": str(timezone.now())}
