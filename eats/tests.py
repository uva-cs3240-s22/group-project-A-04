import datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from .models import Recipe

# Create your tests here.

# manage.py test polls looks for tests in the polls app
# finds subclass of the TestCase class
# creates special database for testing
# looks for test methods— one whose names begin with test
# runs the functions below, returns results of tests through various asserts

# Good rules-of-thumb include having:
# a separate TestClass for each model or view
# a separate test method for each set of conditions you want to test
# test method names that describe their function from the tutorial

# Remember: no code can be pushed to main without tests!

class SampleTests(TestCase):

    # sample test that always returns true
    def test_true(self):
        """
        This sample test always returns True.
        """
        self.assertTrue("Alright, who changed this assertion to False out of spite?", True)


class RecipeModelTests(TestCase):
    r = None

    def setUp(self):
        global r
        r = Recipe(title="Potatoes")

    # recipes have title
    def test_title(self):
        """
        Checks that recipe has title
        """
        global r
        self.assertIs("Recipe constructor does not set title to that passed into the function", r.title, "Potatoes")

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