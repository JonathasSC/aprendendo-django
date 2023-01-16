from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse('Você está voltando na questão de número %s' % question_id)
