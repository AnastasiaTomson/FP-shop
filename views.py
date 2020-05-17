from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')