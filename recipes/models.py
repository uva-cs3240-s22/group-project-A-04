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
from mysite.storage_backends import MediaStorage


"""
Recipe model
Model containing name, description, procedure, publication date,
modification date, and author.
"""
class Recipe(models.Model):
    # Recipe content fields
    recipe_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    
    # Publication information fields
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    """reference the main user model anyways because allauth is like that
    see: https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    default value is primary key of a generic user, but note that this is will not migrate since it is null
    changed to one to one such that each recipe can only have one author"""
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


"""
Recipe Image model
Contains the image for a parent recipe
"""
class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(storage=MediaStorage)


"""
Ingredients model
Contains parent recipe, ingredient name, and ingredient quantity
"""
class Ingredient(models.Model):
    # Ingredient content fields
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.ingredient_name + ",  " + self.quantity
