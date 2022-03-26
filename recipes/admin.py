# recipes/admin.py
# 
# admin module for recipes app

# Importing from Django library
from django.contrib import admin

# Importing models from local files
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'recipe_name']
    list_display = ('recipe_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['recipe_name']
    

admin.site.register(Recipe, RecipeAdmin)

