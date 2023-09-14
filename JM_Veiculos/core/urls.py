from django.urls import path

from .views import index, moto, carro


urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='home'),
    path('carro', carro, name='carro'),
    path('moto', moto, name='moto'),
]
