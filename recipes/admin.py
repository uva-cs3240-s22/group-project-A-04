# recipes/admin.py
# 
# admin module for recipes app

# Importing from Django library
from django.contrib import admin

# Importing models from local files
from .models import Recipe, Ingredient, RecipeImage


class RecipeInLine(admin.TabularInline):
    model = Recipe
    extra = 1


class IngredientInline(admin.TabularInline):
    # make ingredients like choices in polls app
    model = Ingredient
    extra = 1


class RecipeImageInline(admin.TabularInline):
    # make ingredients like choices in polls app
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['recipe_name', 'description']}),
        (None,                  {'fields': ['author']}),
        (None,                  {'fields': ['procedure']}),
        # date information removed since these fields are no longer editable as auto-now/add is true
        # ('Date information',    {'fields': ['pub_date', 'mod_date'], 'classes':['collapse']}),
    ]
    inlines = [RecipeInLine, IngredientInline, RecipeImageInline]
    list_display = ('recipe_name', 'pub_date', 'mod_date')
    list_filter = ['pub_date', 'mod_date']
    search_fields = ['recipe_name', 'description', 'procedure']
    

admin.site.register(Recipe, RecipeAdmin)

