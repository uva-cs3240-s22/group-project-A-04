import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# each question has a question text and a publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # change string representation to show question_text
    def __str__(self):
        return self.question_text

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

# each choice has its own text and a vote tally
# in addition to being associated with a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # change string representation to show choice text
    def __str__(self):
        return self.choice_text

# each model is a class with subclass Model
# each has its own class variables --> database fields in the model

# each field is an instance of a Field class
# specified by a given type (hehe take that regular Python)

# note the first positional argument to any Field creates a human-readable name
# this doubles as documentation, but if not passed, the regular variable name
# will be used --> question is named "Question", but question_text is just question_text

# deepthought model
class DeepThought(models.Model):
    # make a title field limited to 200 chars (just to match the questions and choices)
    title = models.CharField(max_length=200)
    # text field goes into a text field with a higher default max number of characters
    text = models.TextField()

    # string representation shows title
    def __str__(self):
        return self.title

    # # make the createview work???
    # def get_absolute_url(self):
    #     return reverse('deepthoughts', kwargs={'pk': self.pk})
