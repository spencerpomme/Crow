from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word


def index(request):
    """
    Homepage view.
    :param request: request
    :return: rendered page
    """
    template = loader.get_template('wordcards/index.html')
    context = {
        'title': "wtf??",
        'project_name': "Crow"
    }
    return HttpResponse(template.render(context, request))


def card(request):
    """
    Card view.
    :param request: request
    :return: rendered page
    """
    context = {
        'word_list_name': "Word List 1",
    }
    return render(request, 'wordcards/card.html', context)


def gate(request):
    """
    View before entering card view.
    :param request: request
    :return: rendered page
    """
    pass
