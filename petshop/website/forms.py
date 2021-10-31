from petshop.models import Clientes
from django import forms

# Formulário de inserção usando ModelForm.
class InsereClientesForm(forms.ModelForm):
    class Meta:
        # Modelo que o Django deve pegar os campos.
        model = Clientes
        # Os campos que estarão no formulário serão apresentados através do atributo fields.
        fields = [
            'nome',
            'cpf',
            'telefone',
            'email',
            'endereco'
        ]
