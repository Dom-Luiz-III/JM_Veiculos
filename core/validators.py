import re
from django.core.exceptions import ValidationError

def validate_placa(value):
    formato_placa = r'^([A-Z]{3}\d{4}|[A-Z]{3}\d{1}[A-Z]\d{2})$'
    if not re.match(formato_placa, value):
        raise ValidationError("O formato da placa é inválido. Deve seguir o formato 'XXX9999' ou 'XXX9X99'.")