from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
# Create your views here.


def index(request):
    # DATA
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # DEFINE CONTEXT
    context = {
        'latest_questions': latest_questions,
    }
    # SEND RESPONSE
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    # GET THE QUESTION BY ITS ID
    question = get_object_or_404(Question, pk=question_id)
    # DEFINE THE CONTEXT WITH THE QUESTION
    context = {
        'question': question
    }
    # RENDER THE TEMPLATE WITH THE REQUEST AND THE CONTEXT
    return render(request, 'polls/details.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/details.html', {'question': question, 'error_message': 'Please select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
