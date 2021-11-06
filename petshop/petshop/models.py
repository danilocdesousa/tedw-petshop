from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

# Mostrar o nome do registro no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.nome
