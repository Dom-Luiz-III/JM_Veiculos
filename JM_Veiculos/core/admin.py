from django.utils.html import format_html
from django.contrib import admin

from .models import Carro, Moto


class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados', 'leilao', 'formas_pagamento', 'display_foto')

    def display_foto(self, obj):
        return format_html('<img src="{}" width="150" height="100" style="border-radius: 10px" />', obj.foto.url)

    display_foto.short_description = 'Foto'

class MotoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados', 'leilao', 'formas_pagamento', 'display_foto')

    def display_foto(self, obj):
        return format_html('<img src="{}" width="150" height="100" style="border-radius: 10px" />', obj.foto.url)

    display_foto.short_description = 'Foto'


admin.site.register(Carro, CarroAdmin)
admin.site.register(Moto, MotoAdmin)
