from django.urls import path

from .views import index, moto, carro, utilitarios, comprar_veiculo

urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='home'),
    path('carro', carro, name='carro'),
    path('moto', moto, name='moto'),
    path('utilitarios', utilitarios, name='utilitarios'),
    path('comprar_veiculo/<str:veiculo_tipo>/<int:veiculo_id>/', comprar_veiculo, name='comprar_veiculo'),
]
