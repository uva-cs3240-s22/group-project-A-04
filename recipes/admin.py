# recipes/admin.py
# 
# admin module for recipes app

# Importing from Django library
from django.contrib import admin

# Importing models from local files
from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    # make ingredients like choices in polls app
    model = Ingredient
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['recipe_name']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [IngredientInline]
    list_display = ('recipe_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['recipe_name']
    

admin.site.register(Recipe, RecipeAdmin)

