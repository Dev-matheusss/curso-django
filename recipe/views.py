from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'recipe/home.html')


def contato(request):
    return HttpResponse('contato3')


def sobre(request):
    return HttpResponse('sobre4')