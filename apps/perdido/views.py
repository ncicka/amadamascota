from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Perdido

# Create your views here.

def perdido(request):
    return HttpResponse("Estoy perdido")

class PerdidoListView(generic.ListView):
    model = Perdido
    template_name = 'perdido/lista_perdido.html'