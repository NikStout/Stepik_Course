from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from random import randint
from .data import tours


def main_view(request):
    tours_random = {}
    while len(tours_random) < 6:
        a = randint(1, 16)
        if a in tours_random:
            continue
        else:
            tours_random[a] = tours[a]
    context = {"tours_random": tours_random}
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure: str):
    return render(request, 'tours/departure.html')


def tour_view(request, id: int):
    context = {"tours": tours[id]}
    return render(request, 'tours/tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
