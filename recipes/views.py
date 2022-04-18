"""
recipes/views.py
This file contains definitions of how specific models are viewed
"""

# Imports from Django library
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# model form for query sets
from django.forms.models import inlineformset_factory
# cited from this youtube tutorial: https://youtu.be/6wHx-X1tEiY

# Importing models from current directory
from .models import Recipe, Ingredient, RecipeImage
from .forms import RecipeForm, IngredientForm, RecipeImageForm

# make login required before any of these views can be accessed taken from this
# YouTube video: https://youtu.be/PICYTJqj__o


"""
Recipe index view
Displays all of the recipes using 'recipes/index.html' and inserts the the view
into an object_list called 'latest_recipe_list'
"""
class RecipeIndex(ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:5]


"""
Recipe detail view
Displays the details of the recipe ysing 'recipes/detail.html'
"""
class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipe.objects


"""
Recipe modification view
Displays the recipe modification page using 'recipes/edit.html'
"""
class RecipeModify(UpdateView):
    model = Recipe
    template_name = 'recipes/edit.html'


# class RecipeCreate(CreateView):
#     model = Recipe
#     template_name = 'recipes/form.html'
#     fields = ["recipe_name", "description", "procedure"]
#
#
#     def get_success_url(self):
#         return reverse('recipes:index')
#
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


@login_required
def recipe_create_view(request):
    # specify template
    template = 'recipes/form.html'

    # make a form for recipes and ingredients
    recipe_form = RecipeForm(request.POST or None)
    recipe_image_form = RecipeImageForm(request.POST or None, request.FILES)
    # ingredient_form = IngredientForm(request.POST or None)

    # make instance of Formset
    IngredientInlineFormset = inlineformset_factory(Recipe, Ingredient,
                                                    fields=('ingredient_name', 'quantity'),
                                                    extra=1)
    ingredient_formset = IngredientInlineFormset(request.POST or None)

    # for loading html
    context = {
        "recipe_form": recipe_form,
        "recipe_image_form": recipe_image_form,
        # "ingredient_form": ingredient_form,
        "ingredient_formset": ingredient_formset,
    }

    # check that the form is valid, if so, submit
    if all([recipe_form.is_valid(), recipe_image_form.is_valid(), ingredient_formset.is_valid()]):
        recipe = recipe_form.save(commit=False)     # commit = False does not add to DB
        recipe.author = request.user

        recipe_image = recipe_image_form.save(commit=False)
        recipe_image.recipe = recipe

        for ingredient_form in ingredient_formset:
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()

        recipe.save()
        recipe_image.save()

        # confirmation message
        context['message'] = 'Recipe saved!'

        return redirect(reverse('recipes:index'))

    # otherwise, redirect to original form
    return render(request, template, context)

# cited from this youtube tutorial:
# https://youtu.be/6wHx-X1tEiY
@login_required
def recipe_update_view(request, pk=None):
    # specify template
    template = 'recipes/form.html'

    # get recipe
    recipe = get_object_or_404(Recipe, pk=pk)

    # make a form for recipes and ingredients
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    # get first image found, might change this inline later
    recipe_image_form = RecipeImageForm(request.POST or None, request.FILES, instance=RecipeImage.objects.filter(recipe=recipe)[0])

    # ingredient_form = IngredientForm(request.POST or None)

    # make instance of Formset
    IngredientInlineFormset = inlineformset_factory(Recipe, Ingredient,
                                                    fields=('ingredient_name', 'quantity'),
                                                    extra=1)
    ingredient_formset = IngredientInlineFormset(request.POST or None, instance=recipe)

    # for loading html
    context = {
        "recipe_form": recipe_form,
        "recipe_image_form": recipe_image_form,
        # "ingredient_form": ingredient_form,
        "ingredient_formset": ingredient_formset,
        "recipe": recipe,
    }

    # check that the form is valid, if so, submit
    if all([recipe_form.is_valid(), ingredient_formset.is_valid()]):
        recipe = recipe_form.save(commit=False)     # commit = False does not add to DB
        recipe.author = request.user

        recipe_image = recipe_image_form.save(commit=False)
        recipe_image.recipe = recipe

        for ingredient_form in ingredient_formset:
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()

        recipe.save()
        recipe_image.save()

        # confirmation message
        context['message'] = 'Recipe saved!'

        return redirect(reverse('recipes:detail', kwargs={"pk":recipe.pk}))

    # otherwise, redirect to original form
    return render(request, template, context)
