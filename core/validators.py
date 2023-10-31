import re
from django.core.exceptions import ValidationError
from django.apps import apps

def validate_placa_unica(value):
    Carro = apps.get_model('core', 'Carro')
    Moto = apps.get_model('core', 'Moto')
    Utilitarios = apps.get_model('core', 'Utilitarios')

    if Carro.objects.filter(placa=value).exists() or \
       Moto.objects.filter(placa=value).exists() or \
       Utilitarios.objects.filter(placa=value).exists():
        raise ValidationError("Esta placa já está em uso por outro veículo.")


def validate_placa(value):
    formato_placa = r'^([A-Z]{3}\d{4}|[A-Z]{3}\d{1}[A-Z]\d{2})$'
    if not re.match(formato_placa, value):
        raise ValidationError("O formato da placa é inválido. Deve seguir o formato 'XXX9999' ou 'XXX9X99'.")