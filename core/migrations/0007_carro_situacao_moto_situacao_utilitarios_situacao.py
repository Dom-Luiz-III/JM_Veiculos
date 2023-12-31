# Generated by Django 4.2.4 on 2023-09-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_utilitarios_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='situacao',
            field=models.CharField(choices=[('venda', 'A Venda'), ('vendido', 'Vendido')], default='venda', max_length=20, verbose_name='Situação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moto',
            name='situacao',
            field=models.CharField(choices=[('venda', 'A Venda'), ('vendido', 'Vendido')], default='venda', max_length=20, verbose_name='Situação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilitarios',
            name='situacao',
            field=models.CharField(choices=[('venda', 'A Venda'), ('vendido', 'Vendido')], default='venda', max_length=20, verbose_name='Situação'),
            preserve_default=False,
        ),
    ]
