from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Carro(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[
                              ('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[
                                        ('vista', 'A Vista'), ('parcelado', 'Parcelado'), ('consorcio', 'Consórcio')])
    situacao = models.CharField('Situação', max_length=20, choices=[
                                ('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField(
        'Foto', upload_to='carros/', null=True, blank=True)

    def __str__(self):
        return self.modelo

    # Comando para mostrar uma miniatura da imagem no admin do Django. 
    # Se a imagem existir, ela será exibida. Caso contrário, a imagem padrão sem_foto.jpg será exibida:
    def foto_tag(self):
        if self.foto:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        else:
            default_image_path = 'core/images/sem_foto.jpg'
            return mark_safe('<img src="{}" width="50" height="50" />'.format(default_image_path))

    foto_tag.short_description = 'Imagem'

    # Verifica se a foto está em branco e, se estiver, atribui o caminho da imagem padrão
    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = 'carros/sem_foto.jpg'

        super(Carro, self).save(*args, **kwargs)


class Moto(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[
                              ('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[
                                        ('vista', 'A Vista'), ('parcelado', 'Parcelado'), ('consorcio', 'Consórcio')])
    situacao = models.CharField('Situação', max_length=20, choices=[
                                ('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField('Foto', upload_to='motos/', null=True, blank=True)

    def __str__(self):
        return self.modelo

    # Comando para mostrar uma miniatura da imagem no admin do Django. 
    # Se a imagem existir, ela será exibida. Caso contrário, a imagem padrão sem_foto.jpg será exibida:
    def foto_tag(self):
        if self.foto:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        else:
            default_image_path = 'core/images/sem_foto.jpg'
            return mark_safe('<img src="{}" width="50" height="50" />'.format(default_image_path))

    foto_tag.short_description = 'Imagem'

    # Verifica se a foto está em branco e, se estiver, atribui o caminho da imagem padrão
    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = 'motos/sem_foto.jpg'

        super(Moto, self).save(*args, **kwargs)


class Utilitarios(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    ano_fabricacao = models.IntegerField('Ano de Fabricação')
    estado = models.CharField('Estado', max_length=20, choices=[
                              ('novo', 'Novo'), ('usado', 'Usado')])
    km_rodados = models.PositiveIntegerField('Km Rodados')
    leilao = models.BooleanField('Passagem por Leilão')
    formas_pagamento = models.CharField('Formas de Pagamento', max_length=20, choices=[
                                        ('vista', 'A Vista'), ('parcelado', 'Parcelado'), ('consorcio', 'Consórcio')])
    situacao = models.CharField('Situação', max_length=20, choices=[
                                ('venda', 'A Venda'), ('vendido', 'Vendido')])
    placa = models.CharField('placa', max_length=7)
    foto = models.ImageField(
        'Foto', upload_to='utilitarios/', null=True, blank=True)

    def __str__(self):
        return self.modelo

    # Comando para mostrar uma miniatura da imagem no admin do Django. 
    # Se a imagem existir, ela será exibida. Caso contrário, a imagem padrão sem_foto.jpg será exibida:
    def foto_tag(self):
        if self.foto:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.foto.url))
        else:
            default_image_path = 'core/images/sem_foto.jpg'
            return mark_safe('<img src="{}" width="50" height="50" />'.format(default_image_path))

    foto_tag.short_description = 'Imagem'

    # Verifica se a foto está em branco e, se estiver, atribui o caminho da imagem padrão
    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = 'utilitarios/sem_foto.jpg'

        super(Utilitarios, self).save(*args, **kwargs)


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
