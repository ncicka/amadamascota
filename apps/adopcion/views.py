from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def adopcion(request):
    return HttpResponse("Quiero dar en Adopción")
