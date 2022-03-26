from django.contrib import admin

# Register your models here.

# tells the admin that Questions have an admin interface
from .models import Question, Choice, DeepThought

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

    # displays individual fields of the model, and other methods
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # add filter option by date of publishing
    list_filter = ['pub_date']
    # note Django auto generates filter options depending on the field type

    # search fields limited to just question text (for better searching)
    search_fields = ['question_text']

    # feel free to change list pagination
    # search boxes
    # filters
    # date-hierarchies
    # and column header ordering as you see fit.

admin.site.register(Question, QuestionAdmin)


class DeepThoughtAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text']}),
    ]

    # displays individual fields of the model, and other methods
    list_display = ('title', 'text')

    # add filter option by text
    list_filter = ['text']
    # note Django auto generates filter options depending on the field type

    # search fields limited to just title (for better searching)
    search_fields = ['title']

    # feel free to change list pagination
    # search boxes
    # filters
    # date-hierarchies
    # and column header ordering as you see fit.


admin.site.register(DeepThought, DeepThoughtAdmin)
