# Importação das funções definidas no arquivo views.py.
from django.urls import path
from website.views import IndexTemplateView, ClientesListView, ClientesUpdateView

app_name = 'website'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),
    
    # GET /clientes
    path('clientes/', ClientesListView.as_view(), name="lista_clientes"),
    
    # Para atualizar o objeto, devemos buscá-lo via 'id' ou 'slug'. Também pode ser atualizado através do método get_object().
    # GET/POST /funcionario/{pk do objeto}
    path('clientes/<pk>', ClientesUpdateView.as_view(), name = "atualiza_clientes"),
]
