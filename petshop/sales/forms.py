from petshop.models import Sales
from django import forms

# Formulário de inserção usando ModelForm.
class InsereSalesForm(forms.ModelForm):
    class Meta:
        # Modelo que o Django deve pegar os campos.
        model = Sales
        # Os campos que estarão no formulário serão apresentados através do atributo fields.
        fields = [
            'cliente',
            'pet',
            'servico',
            'preco',
            'data'
        ]
