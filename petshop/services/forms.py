from petshop.models import Services
from django import forms

# Formulário de inserção usando ModelForm.
class InsereServicesForm(forms.ModelForm):
    detalhes = forms.CharField(label="Observações", widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        # Modelo que o Django deve pegar os campos.
        model = Services
        # Os campos que estarão no formulário serão apresentados através do atributo fields.
        fields = [
            'nome',
            'preco',
            'detalhes'
        ]
