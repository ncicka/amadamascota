# Adopcion
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.adopcion, name="Adopcion"),
]