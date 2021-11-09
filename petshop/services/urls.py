# Importação das funções definidas no arquivo views.py.
from django.urls import path
from services.views import ServicesCreateView

app_name = 'services'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('cadastrar/', ServicesCreateView.as_view(),
         name="cadastra_services"),
]
