# Importação das funções definidas no arquivo views.py.
from django.urls import path
from pets.views import PetsCreateView

app_name = 'pets'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('cadastrar/', PetsCreateView.as_view(), name="cadastra_pets"),
]
