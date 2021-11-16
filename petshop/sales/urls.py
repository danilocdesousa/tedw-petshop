# Importação das funções definidas no arquivo views.py.
from django.urls import path
from sales.views import SalesCreateView, SalesListView,SalesUpdateView, SalesDeleteView

app_name = 'sales'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('cadastrar/', SalesCreateView.as_view(), name="cadastra_sales"),

     # GET /listar
    path('listar/', SalesListView.as_view(), name="lista_sales"),

    # Para atualizar o objeto, devemos buscá-lo via 'id' ou 'slug'. Também pode ser atualizado através do método get_object().
    # GET/POST /sales/{pk do objeto}
    path('sales/<pk>', SalesUpdateView.as_view(), name = "atualiza_sales"),
    
    # Para deletar o objeto, o procedimento é parecido com o de atualização.
    # GET/POST /sales/excluir/{pk do objeto}
    path('sales/excluir/<pk>', SalesDeleteView.as_view(), name="deleta_sales"),
]