from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def perdido(request):
    return HttpResponse("Estoy perdido")
