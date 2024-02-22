from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Logic here

def pong(request):
    return render(request, 'pong/test.html')

# Faire une room par game ?