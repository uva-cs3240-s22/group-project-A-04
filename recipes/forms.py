from django import forms

from .models import Recipe, Ingredient, RecipeImage


# The code for these forms were taken from this youtube video:
# https://youtu.be/PICYTJqj__o


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'description', 'procedure']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'quantity']


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', ]