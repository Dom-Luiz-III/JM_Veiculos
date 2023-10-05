from django.db import models

class Carro(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[('vista', 'A Vista'), ('parcelado', 'Parcelado')])
    situacao = models.CharField('Situação', max_length=20, choices=[('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField('Foto', upload_to='carros/', null=True, blank=True)

    def __str__(self):
        return self.modelo

class Moto(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[('vista', 'A Vista'), ('parcelado', 'Parcelado')])
    situacao = models.CharField('Situação', max_length=20, choices=[('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField('Foto', upload_to='motos/', null=True, blank=True)


    def __str__(self):
        return self.modelo

class Utilitarios(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[('vista', 'A Vista'), ('parcelado', 'Parcelado')])
    situacao = models.CharField('Situação', max_length=20, choices=[('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField('Foto', upload_to='utilitarios/', null=True, blank=True)

    def __str__(self):
        return self.modelo
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome