# Imports from Django library
import sys
sys.path.append("..")

from re import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q

# model form for query sets
from django.forms.models import inlineformset_factory
# cited from this youtube tutorial: https://youtu.be/6wHx-X1tEiY

# Importing models from current directory
from recipes.models import Recipe, Ingredient, RecipeImage
from recipes.forms import RecipeForm, RecipeImageForm, IngredientInlineFormset

class HomeIndex(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:3]