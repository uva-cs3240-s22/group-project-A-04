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
from itertools import chain


class HomeIndex(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        l3 = Recipe.objects.all()
        l1 = l3.order_by('likes')[:3]
        l2 = l3.order_by('-pub_date')[:3]
        return list(chain(l2,l1))
    
    # def get_context_data(self, **kwargs):
    #     context = super(HomeIndex, self).get_context_data(**kwargs)
    #     context['popular_recipe_list'] = Recipe.objects.order_by("likes")[:3]
    #     # Add any other variables to the context here
    #     ...
    #     return context

