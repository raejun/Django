# polls/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice

# http://127.0.0.1:8000/polls/
def index(request):
    latest_question_list = Question.objects.all()
    print(latest_question_list)
    context = {'latest_question_list':latest_question_list}
    return render(request, 'index.html', context)

# http://127.0.0.1:8000/polls/2/
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'detail.html', {'question':question})

# http://127.0.0.1:8000/polls/2/vote/
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()  # UPDATE
        # return HttpResponse('ok2')
        return HttpResponseRedirect('/polls/' + question_id + '/results/')

# http://127.0.0.1:8000/polls/2/results/
def results(request, question_id):
    # "SELECT * FROM polls_question WHERE question_id=2"
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'results.html', {'question':question})
