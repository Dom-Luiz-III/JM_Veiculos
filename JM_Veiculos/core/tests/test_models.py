from django.test import TestCase
from core.models import Carro
from core.models import Moto
from core.models import Utilitarios

class CarroModelTest(TestCase):

    def test_tipo_de_dado(self):
        carro = Carro(
            modelo='Toyota Camry',
            marca='Toyota',
            ano_fabricacao=2023,
            estado='novo',
            km_rodados=10000,
            leilao=False,
            formas_pagamento='vista',
            situacao='vendido',
            placa='ABC123'
        )

        # Verifica se o tipo de dado de cada campo é o esperado
        self.assertIsInstance(carro.modelo, str)
        self.assertIsInstance(carro.marca, str)
        self.assertIsInstance(carro.ano_fabricacao, int)
        self.assertIsInstance(carro.estado, str)
        self.assertIsInstance(carro.km_rodados, int)
        self.assertIsInstance(carro.leilao, bool)
        self.assertIsInstance(carro.formas_pagamento, str)
        self.assertIsInstance(carro.situacao, str)
        self.assertIsInstance(carro.placa, str)

class MotoModelTest(TestCase):

    def test_tipo_de_dado(self):
        moto = Moto(
            modelo='Honda CBR1000RR',
            marca='Honda',
            ano_fabricacao=2022,
            estado='usado',
            km_rodados=7000,
            leilao=True,
            formas_pagamento='parcelado',
            situacao='A venda',
            placa='ABC123'
        )


        # Verifica se o tipo de dado de cada campo é o esperado
        self.assertIsInstance(moto.modelo, str)
        self.assertIsInstance(moto.marca, str)
        self.assertIsInstance(moto.ano_fabricacao, int)
        self.assertIsInstance(moto.estado, str)
        self.assertIsInstance(moto.km_rodados, int)
        self.assertIsInstance(moto.leilao, bool)
        self.assertIsInstance(moto.formas_pagamento, str)
        self.assertIsInstance(moto.situacao, str)
        self.assertIsInstance(moto.placa, str)


class UtilitariosModelTest(TestCase):

    def test_tipo_de_dado(self):
        utilitarios = Utilitarios(
            modelo='Ford Transit',
            marca='Ford',
            ano_fabricacao=2022,
            estado='usado',
            km_rodados=7000,
            leilao=True,
            formas_pagamento='parcelado',
            situacao='A venda',
            placa='ABC1E03'
        )

        # Verifica se o tipo de dado de cada campo é o esperado
        self.assertIsInstance(utilitarios.modelo, str)
        self.assertIsInstance(utilitarios.marca, str)
        self.assertIsInstance(utilitarios.ano_fabricacao, int)
        self.assertIsInstance(utilitarios.estado, str)
        self.assertIsInstance(utilitarios.km_rodados, int)
        self.assertIsInstance(utilitarios.leilao, bool)
        self.assertIsInstance(utilitarios.formas_pagamento, str)
        self.assertIsInstance(utilitarios.situacao, str)
        self.assertIsInstance(utilitarios.placa, str)

# verificar se uma placa de carro segue o formato Mercosul, que consiste em três letras, um número, uma letra e dois números.
# retorna True se a placa estiver no formato correto e False caso contrário.
    def verificar_placa_mercosul(self, placa):
        letras = placa[:3]
        numero1 = placa[3]
        letra = placa[4]
        numero2 = placa[5:]

        if len(placa) != 7:
            return False

        if not isinstance(letras, str):
            return False

        if not isinstance(numero1, int):
            return False

        if not isinstance(letra, str):
            return False

        if not isinstance(numero2, int):
            return False

        return True

# No método test_verificar_placa_mercosul ele testa o método verificar_placa_mercosul com duas placas, uma válida e uma inválida
    def test_verificar_placa_mercosul(self):
        placa_valida = "ABC1D23"
        placa_invalida = "ABC12D34"

        self.assertTrue(self.verificar_placa_mercosul(placa_valida))
        self.assertFalse(self.verificar_placa_mercosul(placa_invalida))

# python manage.py test core.tests

