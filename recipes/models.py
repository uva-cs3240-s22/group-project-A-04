# recipes/models.py
# 
# models for recipes app

# Import from python stdlib
import datetime

# Import from Django Library
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User     # for recipe authors


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    # add option description field for recipe
    description = models.TextField(blank=True)

    # procedure can be a list of steps or paragraphs --> just textfield
    procedure = models.TextField(blank=True)

    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

    # reference the main user model anyways because allauth is like that
    # see: https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    # default value is primary key of a generic user --> this will have to changed in admin later
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User().pk)

    def __str__(self):
        return self.recipe_name

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# each ingredient has its own name and quantity
# in addition to being associated with a recipe
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

    # change string representation to show choice text
    def __str__(self):
        return self.ingredient_name + ",  " + self.quantity