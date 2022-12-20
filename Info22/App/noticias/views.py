from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia
# Create your views here.

class Noticialv(ListView):
    model = Noticia
    template_name = 'noticia/nview.html'
    