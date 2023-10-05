from django.urls import path

from .views import contato, index, moto, carro, politica, utilitarios, comprar_veiculo

urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='home'),
    path('carro', carro, name='carro'),
    path('moto', moto, name='moto'),
    path('politicas', politica, name='politicas'),
    path('utilitarios', utilitarios, name='utilitarios'),
    path('contato/', contato, name='contato'),
    path('comprar_veiculo/<str:veiculo_tipo>/<int:veiculo_id>/', comprar_veiculo, name='comprar_veiculo'),
]
