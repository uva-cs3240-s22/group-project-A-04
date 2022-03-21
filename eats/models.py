import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # change string representation to show question_text
    def __str__(self):
        return self.title

    # improves display of was_published_recently() in admin page
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    # returns a boolean indicating that question was published within
    # the past day
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now