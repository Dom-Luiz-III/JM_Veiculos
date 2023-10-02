from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Carro
from .models import Moto
from .models import Utilitarios


def index(request):
    carros = Carro.objects.all()
    motos = Moto.objects.all()
    utilitarios = Utilitarios.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'carros': carros,
        'motos': motos,
        'utilitarios': utilitarios
    }
    return render(request, 'index.html', context)


def moto(request):
    motos = Moto.objects.all()

    context = {
        'motos': motos
    }

    return render(request, 'moto.html', context)

def carro(request):
    carros = Carro.objects.all()

    context = {
        'carros': carros,
    }
    return render(request, 'carro.html', context)

def utilitarios(request):
    utilitarios = Utilitarios.objects.all()

    context = {
        'utilitarios': utilitarios,
    }
    return render(request, 'utilitarios.html', context)