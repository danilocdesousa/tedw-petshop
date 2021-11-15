from django.db import models


# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        verbose_name='CPF',
        unique=True
    )

    telefone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Telefone'
    )

    email = models.CharField(
        max_length=100,
        verbose_name='Email'
    )

    endereco = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Endereço'
    )

    class Meta:
        verbose_name_plural = 'Clientes'

# Mostrar o nome do cliente no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.nome


class Services(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Preço'
    )

    detalhes = models.TextField(verbose_name='Observações')

    class Meta:
        verbose_name_plural = 'Serviços'

# Mostrar o nome do cliente no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.nome


class Pet(models.Model):
    SEX = (
        ('F', 'Fêmea'),
        ('M', 'Macho'),
        ('N', 'Não informado')
    )

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    especie = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Espécie/tipo'
    )

    raca = models.CharField(
        max_length=255,
        verbose_name='Raça'
    )

    sexo = models.CharField(
        max_length=20,
        # Usar o select.
        choices=SEX,  # Constante SEX.
        verbose_name='Sexo'
    )

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='Cliente')

    notas = models.TextField(verbose_name='Observações')

    class Meta:
        verbose_name_plural = 'Pets'

    # Mostrar o nome do cliente no Django administration em vez de mostrar o ID. Ou seja, o método str determina como o objeto vai ser impresso.
    def __str__(self):
        return self.nome


class Sales(models.Model):

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name='Cliente')

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Pet')

    servico = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Serviço')

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Preço'
    )

    data = models.DateField(verbose_name='Data da venda')

    class Meta:
        verbose_name_plural = 'Vendas'

# Mostrar o nome do cliente no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.cliente
