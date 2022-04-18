from django import forms

from .models import Recipe, Ingredient, RecipeImage


# The code for these forms were taken from this youtube video:
# https://youtu.be/PICYTJqj__o


"""
Recipe Form
Contains the meta data for a recipe
"""
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'description', 'procedure']


"""
Recipe Image Form
Contains the meta data for images within parent recipes
"""
class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', ]


"""
Ingredient Form
Contains the meta data for the ingredients within a parent recipe
"""
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'quantity']

