from django.utils.html import format_html
from django.contrib import admin

from .models import Carro, Contato, Moto, Utilitarios


class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa', 'display_foto')

    def display_foto(self, obj):
        return format_html('<img src="{}" width="150" height="100" style="border-radius: 10px" />', obj.foto.url)

    display_foto.short_description = 'Foto'

    list_filter = ('marca', 'situacao','estado')

    search_fields = ['modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa']
    
    list_per_page = 10


class MotoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa', 'display_foto')

    def display_foto(self, obj):
        return format_html('<img src="{}" width="150" height="100" style="border-radius: 10px" />', obj.foto.url)

    display_foto.short_description = 'Foto'

    list_filter = ('marca', 'situacao','estado')

    search_fields = ['modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa']
    
    list_per_page = 10


class UtilitariosAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa', 'display_foto')

    def display_foto(self, obj):
        return format_html('<img src="{}" width="150" height="100" style="border-radius: 10px" />', obj.foto.url)

    display_foto.short_description = 'Foto'

    list_filter = ('marca', 'situacao','estado')

    search_fields = ['modelo', 'marca', 'ano_fabricacao', 'estado', 'km_rodados',
                    'leilao', 'formas_pagamento', 'situacao', 'placa']
    
    list_per_page = 10

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'mensagem') 

    list_filter= ('mensagem',)

    search_fields = ['nome', 'email', 'telefone']

    list_per_page = 10

admin.site.register(Carro, CarroAdmin)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Utilitarios, UtilitariosAdmin)
admin.site.register(Contato, ContatoAdmin)