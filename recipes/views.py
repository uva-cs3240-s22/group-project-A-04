# recipes/views.py
# 
# views for the recipe app

# Imports from Django library
from re import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q


# Importing models from current directory
from .models import Recipe, Ingredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm, IngredientInlineFormset


# make login required before any of these views can be accessed
# taken from this YouTube video: https://youtu.be/PICYTJqj__o
class ProfileView(ListView):
    model = Recipe
    template_name = 'recipes/profile.html'
    context_object_name = 'liked_recipe_list'

    def get_queryset(self):
        object_list = Recipe.objects.filter(Q(likes__in=[self.request.user]))
        return object_list.order_by('-pub_date')    # order search results by publish date

    # for creating additional context objects
    # cited from here: https://stackoverflow.com/questions/43387875/django-how-to-get-multiple-context-object-name-for-multiple-queryset-from-single
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['created_recipe_list'] = Recipe.objects.filter(Q(author__id=self.request.user.id))
        # Add any other variables to the context here
        ...
        return context


class RecipeIndex(ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-pub_date')[:]

# Gotten from tutorial here https://learndjango.com/tutorials/django-search-tutorial
class SearchResults(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Recipe.objects.filter(
            Q(recipe_name__icontains=query) | Q(description__icontains=query)
        )
        return object_list.order_by('-pub_date')    # order search results by publish date

class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Recipe.objects

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Recipe, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


# like feature referenced from this tutorial:
# https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg
def recipe_like(request, pk):
    post = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse('recipes:detail', kwargs={"pk":post.pk}))

@login_required
def recipe_create_view(request):
    # specify template
    template = 'recipes/form.html'

    # make a form for recipes and ingredients
    recipe_form = RecipeForm(request.POST or None)
    recipe_image_form = RecipeImageForm(request.POST or None, request.FILES)

    # make instance of Formset
    ingredient_formset = IngredientInlineFormset(request.POST or None)

    # for loading html
    context = {
        "recipe_form": recipe_form,
        "recipe_image_form": recipe_image_form,
        "ingredient_formset": ingredient_formset,
    }

    # check that the form is valid, if so, submit
    return validate_and_save_recipe_form(request, template, context, recipe_form, recipe_image_form, ingredient_formset)


# cited from this youtube tutorial:
# https://youtu.be/6wHx-X1tEiY
@login_required
def recipe_update_view(request, pk=None):
    # specify template
    template = 'recipes/form.html'

    # get recipe
    recipe = get_object_or_404(Recipe, pk=pk)

    # check that request user is equal to recipe author, otherwise, redirect back to details page
    if request.user != recipe.author:
        return redirect(reverse('recipes:detail', kwargs={"pk":recipe.pk}))

    # make a form for recipes and ingredients
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    # get first image found, might change this inline later
    recipe_image_form = RecipeImageForm(request.POST or None, request.FILES, instance=RecipeImage.objects.filter(recipe=recipe)[0])


    # make instance of Formset
    ingredient_formset = IngredientInlineFormset(request.POST or None, instance=recipe)

    # for loading html
    context = {
        "recipe_form": recipe_form,
        "recipe_image_form": recipe_image_form,
        "ingredient_formset": ingredient_formset,
        "recipe": recipe,
    }

    # check that the forms are valid, if so, submit
    return validate_and_save_recipe_form(request, template, context, recipe_form, recipe_image_form, ingredient_formset, recipe.parent)

@login_required
def recipe_fork_view(request, pk=None):
    # specify template
    template = 'recipes/form.html'

    # get parent recipe
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.pk = None

    # get parent recipe
    parent_recipe = get_object_or_404(Recipe, pk=pk)

    # check that request user is not equal to parent recipe author, otherwise, redirect back to details page
    if request.user == parent_recipe.author:
        return redirect(reverse('recipes:detail', kwargs={"pk":parent_recipe.pk}))

    # make a form for recipes and ingredients
    recipe_form = RecipeForm(request.POST or None, instance=recipe)

    # get first image found, might change this inline later
    if RecipeImage.objects.filter(recipe=parent_recipe):
        recipe_image_form = RecipeImageForm(request.POST or None, request.FILES, instance=RecipeImage.objects.filter(recipe=parent_recipe)[0])
    else:
        recipe_image_form = RecipeImageForm(request.POST or None, request.FILES)

    # make instance of Formset
    ingredient_formset = IngredientInlineFormset(request.POST or None, instance=parent_recipe)

    # for loading html
    context = {
        "recipe_form": recipe_form,
        "recipe_image_form": recipe_image_form,
        "ingredient_formset": ingredient_formset,
        "parent_recipe": parent_recipe,
    }

    # check that the form is valid, if so, submit
    if all([recipe_form.is_valid(), recipe_image_form.is_valid(), ingredient_formset.is_valid()]):
        recipe = recipe_form.save(commit=False)  # commit = False does not add to DB
        recipe_image = recipe_image_form.save(commit=False)

        recipe.author = request.user
        recipe.parent = parent_recipe
        recipe.save()

        # if forking, clone image
        recipe_image.pk = None
        recipe_image.recipe = recipe
        recipe_image.save()

        for ingredient_form in ingredient_formset:
            if ingredient_form.is_valid():
                ingredient = ingredient_form.save(commit=False)
                # if forking, clone ingredient
                ingredient.pk = None
                ingredient.recipe = recipe
                ingredient.save()

        ingredient_formset.instance = recipe
        ingredient_formset.save()

        # confirmation message
        context['message'] = 'Recipe saved!'

        return redirect(reverse('recipes:detail', kwargs={"pk": recipe.pk}))

    # otherwise, redirect to original form
    return render(request, template, context)

@login_required
def validate_and_save_recipe_form(request, template, context, recipe_form, recipe_image_form, ingredient_formset, parent=None):

    # check that the form is valid, if so, submit
    if all([recipe_form.is_valid(), recipe_image_form.is_valid(), ingredient_formset.is_valid()]):
        recipe = recipe_form.save(commit=False)     # commit = False does not add to DB
        recipe_image = recipe_image_form.save(commit=False)

        recipe.author = request.user
        recipe.parent = parent
        recipe.save()

        recipe_image.recipe = recipe
        recipe_image.save()

        ingredient_formset.instance = recipe
        ingredient_formset.save()

        # confirmation message
        context['message'] = 'Recipe saved!'

        return redirect(reverse('recipes:detail', kwargs={"pk":recipe.pk}))

    # otherwise, redirect to original form
    return render(request, template, context)


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:index')
