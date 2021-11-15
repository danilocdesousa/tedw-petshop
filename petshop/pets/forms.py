from petshop.models import Pet
from django import forms


# Formulário de inserção usando ModelForm.
class InserePetsForm(forms.ModelForm):
    notas = forms.CharField(label="Observações", widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        # Modelo que o Django deve pegar os campos.
        model = Pet
        # Os campos que estarão no formulário serão apresentados através do atributo fields.
        fields = [
            'nome',
            'especie',
            'raca',
            'sexo',
            'notas',
            'cliente'
        ]
