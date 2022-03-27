# recipes/models.py
# 
# models for recipes app

# Import from python stdlib
import datetime

# Import from Django Library
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    # recipe_ingredients = models.CharField(max_length=200)
    # recipe_procedure = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
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