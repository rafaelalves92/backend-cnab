from django.db import models


class Bank(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=127)
    hora = models.TimeField()
    dono_loja = models.CharField(max_length=127)
    nome_loja = models.CharField(max_length=127)
