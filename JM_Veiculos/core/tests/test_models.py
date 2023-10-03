from django.test import TestCase
from core.models import Carro
from core.models import Moto
from core.models import Utilitarios

# execute isso no terminal -  python manage.py test core.tests

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
            placa='OMN9S23'
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

        # Verifica se a placa do carro segue o formato Mercosul
        # (três letras, um número, uma letra e dois números)
        self.assertTrue(self.verificar_placa_mercosul(carro.placa))

    @staticmethod
    def verificar_placa_mercosul(placa):
        # Verifica se a placa tem 7 caracteres
        if len(placa) != 7:
            return False

        # Separa a placa em partes
        letras = placa[:3]  # As três primeiras letras
        numero1 = placa[3]  # O primeiro número
        letra = placa[4]  # A letra no meio
        numero2 = placa[5:]  # Os dois últimos números

        # Verifica se as letras são compostas apenas de caracteres alfabéticos
        if not letras.isalpha() and letra.isalpha():
            return False

        # Verifica se os números são dígitos numéricos dentro de uma string
        if not (numero1.isdigit() and numero2.isdigit()):
            return False

        # Se todas as verificações passarem, a placa é válida
        return True


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
            placa='EAD2I23'
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

        # Verifica se a placa do carro segue o formato Mercosul
        # (três letras, um número, uma letra e dois números)
        self.assertTrue(self.verificar_placa_mercosul(moto.placa))

    @staticmethod
    def verificar_placa_mercosul(placa):
        # Verifica se a placa tem 7 caracteres
        if len(placa) != 7:
            return False

        # Separa a placa em partes
        letras = placa[:3]  # As três primeiras letras
        numero1 = placa[3]  # O primeiro número
        letra = placa[4]  # A letra no meio
        numero2 = placa[5:]  # Os dois últimos números

        # Verifica se as letras são compostas apenas de caracteres alfabéticos
        if not letras.isalpha() and letra.isalpha():
            return False

        # Verifica se os números são dígitos numéricos dentro de uma string
        if not (numero1.isdigit() and numero2.isdigit()):
            return False

        # Se todas as verificações passarem, a placa é válida
        return True


class UtilitariosModelTest(TestCase):
    def test_tipo_de_dado(self):
        # Cria um objeto 'utilitarios' com informações fictícias
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

        # Verifica se a placa do carro segue o formato Mercosul
        # (três letras, um número, uma letra e dois números)
        self.assertTrue(self.verificar_placa_mercosul(utilitarios.placa))

    @staticmethod
    def verificar_placa_mercosul(placa):
        # Verifica se a placa tem 7 caracteres
        if len(placa) != 7:
            return False

        # Separa a placa em partes
        letras = placa[:3]      # As três primeiras letras
        numero1 = placa[3]      # O primeiro número
        letra = placa[4]        # A letra no meio
        numero2 = placa[5:]     # Os dois últimos números

        # Verifica se as letras são compostas apenas de caracteres alfabéticos
        if not letras.isalpha() and letra.isalpha():
            return False

        # Verifica se os números são dígitos numéricos dentro de uma string
        if not (numero1.isdigit() and numero2.isdigit()):
            return False

        # Se todas as verificações passarem, a placa é válida
        return True

