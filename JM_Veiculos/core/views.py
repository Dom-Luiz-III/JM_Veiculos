from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader

from core.forms import ContatoForm

from .models import Carro
from .models import Moto
from .models import Utilitarios
from .models import Contato

from django.contrib.auth import login
from django.shortcuts import render, redirect

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
    motos = Moto.objects.filter(situacao='venda')

    context = {
        'motos': motos
    }

    return render(request, 'moto.html', context)


def carro(request):
    carros = Carro.objects.filter(situacao='venda')

    context = {
        'carros': carros,
    }
    return render(request, 'carro.html', context)


def utilitarios(request):
    utilitarios = Utilitarios.objects.filter(situacao='venda')

    context = {
        'utilitarios': utilitarios,
    }
    return render(request, 'utilitarios.html', context)


# Acões para realizar a compra de veículos:
def comprar_veiculo(request, veiculo_tipo, veiculo_id):
    if veiculo_tipo == 'carro':
        veiculo = get_object_or_404(Carro, pk=veiculo_id)
    elif veiculo_tipo == 'moto':
        veiculo = get_object_or_404(Moto, pk=veiculo_id)
    elif veiculo_tipo == 'utilitarios':
        veiculo = get_object_or_404(Utilitarios, pk=veiculo_id)
    else:
        # Aqui serve pra fazer excessões se os ifs não forem aceitos, caso tenham alguma ideia podem modificar ele aqui
        pass

    if veiculo.situacao == 'venda':
        veiculo.situacao = 'vendido'
        veiculo.save()
        return redirect(f'{veiculo_tipo}')
    else:
        # Aqui ele vai renderizar um pop up quando um veículo estiver indisponível usando JavaScript
        return render(request, f'{veiculo_tipo}.html', {'veiculo': veiculo, 'veiculo_indisponivel': True})
    

#Ação para cadastrar contatos pela página index
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Cadastro realizado!")
    else:
        form = ContatoForm()
    return render(request, 'index.html', {'form': form})
