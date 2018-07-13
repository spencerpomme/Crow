from django.shortcuts import render, redirect
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
    return HttpResponse(template.render(context, request))


def card(request):
    """
    Card view.
    :param request: request
    :return: rendered page
    """
    next_id = None
    try:
        id = request.POST.get("id", "")
    except Exception as e:
        print(e)

    if id < 5:
        next_id = id + 1
        next_word = Word.objects.filter(id=next_id)
        next_word_dict = list(next_word.values())[0]
        context = {
            'hint': "Some sample hint text serving as a compliment to the image stimulation.",
            'word_text': next_word_dict['word_text'],
            'word_def': next_word_dict['word_def'],
        }
        return render(request, 'wordcards/card_s1.html', context)
    else:
        return render(request, 'wordcards/finish.html', None)


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
