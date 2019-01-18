# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path('', views.index),
    # http://127.0.0.1:8000/polls/2/
    path('<question_id>/', views.detail),
    # http://127.0.0.1:8000/polls/2/vote/
    path('<question_id>/vote/', views.vote),
    # http://127.0.0.1:8000/polls/2/results/
    path('<question_id>/results/', views.results),
]
