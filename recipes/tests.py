import datetime

from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.forms import FileField, ImageField
from django.test import TestCase
from django.utils import timezone

from .models import Recipe, RecipeImage


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



class RecipeImageModelTests(TestCase):
    r = None
    i = None

    def setUp(self):
        global r, i
        r = Recipe(recipe_name="Mashed Potatoes")
        i = RecipeImage(recipe=r)

    # recipe images have a recipe
    def test_recipe(self):
        global r, i
        self.assertIs(r, i.recipe,
                      "Recipe images constructor does not set recipe to that passed into the constructor")

    # recipe images have an image
    def test_jpg_image(self):
        global i
        image_path = 'mediafiles/test.jpg'
        image = ImageFieldFile(instance=image_path, name='test.jpg', field=i.image)
        i.image = image
        self.assertIs(image, i.image,
                      "Recipe images constructor does not set image to that passed into the constructor")
