# URLconf for the polls directory

# imports
from django.urls import path
from . import views

# adds app name
app_name = 'polls'

urlpatterns = [
    # map simple Django view to URL
    # ex. /polls/
    path('', views.IndexView.as_view(), name='index'),

    # ex. /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex. /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex. /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # new url for deep thoughts
    path('deepthoughts/', views.DeepThoughtsView.as_view(), name='deepthoughts'),

    # new url for submitting deep thoughts
    path('deepthoughts/deepthink/', views.deepthink, name='deepthink'),

    # new url for viewing all deep thoughts
    path('deepthoughts/list/', views.DeepThoughtsListView.as_view(), name='deepthoughtslist')
]