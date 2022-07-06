from .services import *
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        text = request.POST['text_for_photo']
        json = returns_random_photo(text)
        return JsonResponse(json)
    else:
        return render(request, 'api_convector/home.html')


def random_photo(request, text):
    json = returns_random_photo(text)
    return JsonResponse(json)
