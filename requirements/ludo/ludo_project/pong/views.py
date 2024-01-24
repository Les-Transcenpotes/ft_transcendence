from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse # A terme, retourner des json pas des requetes http !


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")