from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, Image
from .tools import modifyDB
from pprint import pprint


def index(request):
    """
    Homepage view.
    :param request: request
    :return: rendered page
    """
    template = loader.get_template('wordcards/index.html')
    context = {
        'title': "The Crow Project",
        'project_name': "Crow",
        'intro': "Crows are known to have an extraordinary retentive memory, \
        or photographical memory. Scientists discovered that they are very good at binding visual object and concept behind it."
    }
    print(request.GET)
    print(request.POST)
    print(request)
    return HttpResponse(template.render(context, request))


def card(request):
    """
    Card view.
    :param request: request
    :return: rendered page
    """
    print(request.GET)
    context = {
        'hint': "People use it to drink all kinds of beverages, and from time to time cultural symbols are printed on it.",
    }
    return render(request, 'wordcards/card_s1.html', context)


def card2(request):
    """
    Card view.
    :param request: request
    :return: rendered page
    """
    print(request.GET)
    context = {
        'word_text': "mug",
        'word_def': "test string: word definition placeholder.",
    }
    return render(request, 'wordcards/card_s2.html', context)


def gate(request):
    """
    View before entering card view.
    :param request: request
    :return: rendered page
    """
    pass


def finish(request):
    """
    View after finishing card view.
    :param request: request
    :return: rendered page
    """
    pass
