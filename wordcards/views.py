from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
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

@csrf_exempt
def card(request):
    """
    Card view.
    :param request: request
    :return: rendered page
    """
    init = list(Word.objects.filter(id=1).values())[0]

    context = {
        'hint': "Some sample hint text serving as a compliment to the image stimulation.",
        'id': 1,
        'word_text': init['word_text'],
        'word_def': init['word_def'],
    }
    return render(request, 'wordcards/card_s1.html', context)


@csrf_exempt
def update_word(request):
    """
    Only return json
    :param request:
    :return:
    """
    next_id = None
    # print(request)
    try:
        id = request.GET.get("id")
        # print("id ->", id)
    except Exception as e:
        print(e)
    img_urls = ["../media/image/tumbler.jpg",
                "../media/image/goblet.jpg",
                "../media/image/chalice.jpg",
                "../media/image/mug.jpg",
                "../media/image/tankard.jpg",
                "../media/image/crow1.jpg"
                ]
    if id == "":
        id = "1" # in DB index start from 1
    id = int(id)
    if id > 7:
        id = 2
    if id <= 7:
        next_id = id
        next_word = Word.objects.filter(id=next_id)
        # print(next_word)
        next_word_dict = list(next_word.values())[0]
        res = {
            'hint': "Some sample hint text serving as a compliment to the image stimulation.",
            'word_text': next_word_dict['word_text'],
            'word_def': next_word_dict['word_def'],
            'id': next_word_dict['id'],
            'img_url': img_urls[id-1],
        }
        # pprint(res)
        return JsonResponse(res)
    else:
        return redirect("error")


@csrf_exempt
def log_record(request):
    """
    Modify learning record.
    :param request:
    :return:
    """
    remembered = request.POST.get("remembered")
    id = int(request.POST.get("id"))
    print("id--->", type(id), id)
    print("remembered--->", type(remembered), remembered)
    obj = Word.objects.get(id=id)
    if remembered == "true":
        obj.correct_in_row += 1
    else:
        obj.correct_in_row = 0
        obj.forget_count += 1
    print(obj)
    obj.save()
    return render(request, 'wordcards/log.html', None)


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


def error(request):
    """
    View of error
    :param request:
    :return:
    """
    return render(request, 'wordcards/error.html', None)

