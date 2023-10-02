from django.test import TestCase
from core.models import Carro

class CarroModelTest(TestCase):

    def test_tipo_de_dado(self):
        carro = Carro(
            placa='ABC123',
            modelo='Modelo',
            marca='Marca',
            ano_fabricacao=2023,
            estado='novo',
            km_rodados=10000,
            leilao=False,
            formas_pagamento='vista'
        )

        # Verifica se o tipo de dado de cada campo é o esperado
        self.assertIsInstance(carro.placa, str)
        self.assertIsInstance(carro.modelo, str)
        self.assertIsInstance(carro.marca, str)
        self.assertIsInstance(carro.ano_fabricacao, int)
        self.assertIsInstance(carro.estado, str)
        self.assertIsInstance(carro.km_rodados, int)
        self.assertIsInstance(carro.leilao, bool)
        self.assertIsInstance(carro.formas_pagamento, str)

# python manage.py test tests.core