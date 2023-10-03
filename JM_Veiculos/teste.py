from django.test import TestCase
from .models import Carro
from factory import Factory, Faker

class CarroFactory(Factory):
    class Meta:
        model = Carro

  #ainda não coloquei tudo, apenas testando algumas coisas
    marca = Faker('word')
    modelo = Faker('word')
    ano = Faker('year')
    preco = Faker('pydecimal', left_digits=5, right_digits=2)

#aqui botei pra puxar da classe Carro mas no código da gente é veiculo
class CarroModelTestCase(TestCase):
    def setUp(self):
        self.carro = CarroFactory()  # Crie um objeto Carro de teste

    def test_criacao_carro(self):
        # Verifique se o objeto foi salvo no banco de dados
        carros_no_bd = Carro.objects.all()
        self.assertEqual(carros_no_bd.count(), 1)

        # Recupere o objeto do banco de dados
        carro_salvo = carros_no_bd.first()

        # Verifique se os valores salvos correspondem aos valores definidos na fábrica
        self.assertEqual(self.carro.marca, carro_salvo.marca)
        self.assertEqual(self.carro.modelo, carro_salvo.modelo)
        self.assertEqual(self.carro.ano, carro_salvo.ano)
        self.assertEqual(self.carro.preco, carro_salvo.preco)

    def test_str_repr(self):
        # Verifique a representação de string do objeto
        expected_str = f"{self.carro.marca} {self.carro.modelo} ({self.carro.ano})"
        self.assertEqual(str(self.carro), expected_str)
