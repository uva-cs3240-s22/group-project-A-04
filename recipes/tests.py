import datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from .models import Recipe


# Create your tests here.

class RecipeModelTests(TestCase):
    r = None

    def setUp(self):
        global r
        r = Recipe(recipe_name="Mashed Potatoes")

    # recipes have a recipe name
    def test_recipe_name(self):
        """
        Checks that recipe has a recipe name
        """
        global r
        self.assertIs("Mashed Potatoes", r.recipe_name,
                      "Recipe constructor does not set title to that passed into the constructor")

    # recipes have author
    # recipes have publish date
    # recipes have description (optional --> test for this)

    # recipes have list of ingredients/quantities
    # recipes have list of steps/procedure

    # publishing
    # recipes cannot be published without: title, author, ingredients/quantities, and steps
    # recipes can be published without: description
    # only the author can access the URL until it is published

    # editing
    # only the author can edit the recipe
    # editable fields: title, description, ingredients/quantities, steps
    # think about creating a separate update date field?

    # deleting
    # only the author can delete the recipe
    # author should be prompted for a second time before deleting the recipe
