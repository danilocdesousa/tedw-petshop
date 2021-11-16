from petshop.models import Sales
from django import forms
import datetime

# Formulário de inserção usando ModelForm.
class InsereSalesForm(forms.ModelForm):
    data = forms.DateField(label="Data da venda", initial=datetime.date.today)
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
