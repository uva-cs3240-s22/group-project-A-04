
# imports
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question, Choice, DeepThought
from .forms import DeepThoughtForm

# create generic views for index, detail, and results
# each generic view needs to know what model it is acting upon
# this is provided by using the model attribute

# listview displays a list of objects
class IndexView(generic.ListView):
    # sets template name to our existing index.html instead of its default
    template_name = 'polls/index.html'

    # setting this will override the automatically generated context variable
    # which is question_list, but we want 'latest_question_list'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Returns the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# detailview displays a detail page for a particular type of object
# requires primary keys to be called pk, so they have been changed in the urls.py

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes questions that have not been published"""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    # set template name so results looks different than detail pages
    # even if they are the same on the backend
    template_name = 'polls/results.html'

# handles voting for a particular choice in a particular question
# note that this vote function does NOT handle race conditions
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name
        # here it returns ID of the selected choice as a string (POST values are always strings)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # raises a KeyError if choice is not provided in POST data

    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # increment choice count
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button (good coding practice in general)

    # returns the URL of the view we want to pass control to and its variable parts
    # in this case we're going directly to a results page
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# # create generic view for submitting deepthoughts
# class DeepThoughtsView(generic.CreateView):
#     model = DeepThought
#     template_name = 'polls/deepthoughts.html'
#     fields = ['title', 'text']

# create generic view for submitting deepthoughts
class DeepThoughtsView(generic.FormView):
    template_name = 'polls/deepthoughts.html'
    form_class = DeepThoughtForm

# handles deep thought submission
# note that this one doesn't submission
def deepthink(request):
    # save deepthought
    deepthought = DeepThought(title=request.POST['title'], text=request.POST['text'])
    deepthought.save()

    # in this case we're going directly to a results page
    return HttpResponseRedirect(reverse('polls:deepthoughts'))

# create generic view for listing deepthoughts
class DeepThoughtsListView(generic.ListView):
    # set template name
    template_name = 'polls/deepthoughtslist.html'

    def get_queryset(self):
        """Returns all deepthoughts"""
        return DeepThought.objects.all()

    # haha I didn't need this though for some reason if I delete stuff doesn't work
    def get_context_data(self, *, object_list=DeepThought.objects.all(), **kwargs):

        # initialize context and lines to store each set of deepthoughts
        context = super().get_context_data(**kwargs)
        lines = []

        for object in object_list:
            lines.append(object)

        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")

        try:
            show_lines = paginator.page(page)

        except PageNotAnInteger:
            # if given non-integer page, send first page
            show_lines = paginator.page(1)

        except EmptyPage:
            # if page is out of range, deliver last page
            show_lines = paginator.page(paginator.num_pages)

        context["lines"] = show_lines
        return context

    # The above code for centering text was sourced from the views used for the django-bootstrap 5 demo
    # Title: Django-Bootstrap V5 Sample Pagination Views
    # Author: Original: Zostera and Dylan Verheul, Maintained by: Andre Bar'yudin
    # Date: 02/22/2022
    # Code version: 5
    # URL: https://github.com/zelenij/django-bootstrap-v5/blob/main/example/app/views.py
    # Software License: BSD 3-Clause
