# Generated by Django 3.2.8 on 2021-11-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0007_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='notas',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='services',
            name='detalhes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
    ]
