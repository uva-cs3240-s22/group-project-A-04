from django import forms

# model form for query sets
from django.forms.models import inlineformset_factory
# cited from this youtube tutorial:
# https://youtu.be/6wHx-X1tEiY

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

# class IngredientForm(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = ['ingredient_name', 'quantity']


IngredientInlineFormset = inlineformset_factory(Recipe, Ingredient,
                                                fields=('ingredient_name', 'quantity'),
                                                extra=1,
                                                can_delete=True)
