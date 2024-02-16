from django.shortcuts import render
from pong.classes import *

# Create your views here.

from django.http import HttpResponse

# Logic here

def pong(request): # What's "request" ?
    return render(request, 'pong/test.html')

# Faire une room par game ?