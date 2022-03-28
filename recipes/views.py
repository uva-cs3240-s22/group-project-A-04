# recipes/views.py
# 
# views for the recipe app

# Imports from Django library
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone

# Importing models from current directory
from .models import Recipe


class RecipeIndex(ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:5]


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Recipe.objects


class RecipeModify(UpdateView):
    model = Recipe
    template_name = 'recipes/edit.html'

class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'recipes/form.html'
    fields = ["recipe_name", "description", "procedure"]


    def get_success_url(self):
        return reverse('recipes:index')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)