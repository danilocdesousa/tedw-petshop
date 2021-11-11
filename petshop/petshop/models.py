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

    class Meta:
        verbose_name_plural = 'Clientes'

# Mostrar o nome do cliente no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.nome


class Services(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False
    )

    detalhes = models.TextField()

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
        blank=False
    )

    especie = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    raca = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sexo = models.CharField(
        max_length=20,
        # Usar o select.
        choices=SEX,  # Constante SEX.
    )

    notas = models.TextField()

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pets'

    # Mostrar o nome do cliente no Django administration em vez de mostrar o ID. Ou seja, o método str determina como o objeto vai ser impresso.
    def __str__(self):
        return self.nome


class Sales(models.Model):

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    servico = models.ForeignKey(Services, on_delete=models.CASCADE)

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False
    )

    data = models.DateField()

    class Meta:
        verbose_name_plural = 'Vendas'

# Mostrar o nome do cliente no Django administration em vez de mostrar o ID.
    def __str__(self):
        return self.cliente
