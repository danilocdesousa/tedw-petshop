# Importação das funções definidas no arquivo views.py.
from django.urls import path
from website.views import IndexTemplateView, ClientesListView

app_name = 'website'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),
    
    # GET /clientes
    path('clientes/', ClientesListView.as_view(), name="lista_clientes"),
]
