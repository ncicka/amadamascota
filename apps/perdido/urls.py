# Perdidos
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.perdido, name="Perdido"),
    path('lista_perdido/', views.PerdidoListView.as_view(), name = "lista_perdido"),
]