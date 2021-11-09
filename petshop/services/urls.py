# Importação das funções definidas no arquivo views.py.
from django.urls import path
from services.views import ServicesCreateView, ServicesListView, ServicesUpdateView, ServicesDeleteView

app_name = 'services'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('cadastrar/', ServicesCreateView.as_view(), name="cadastra_services"),

    # GET /listar
    path('listar/', ServicesListView.as_view(), name="lista_services"),

    # Para atualizar o objeto, devemos buscá-lo via 'id' ou 'slug'. Também pode ser atualizado através do método get_object().
    # GET/POST /services (services está definido em url.py petshop)/{pk do objeto}
    path('atualizar/<pk>', ServicesUpdateView.as_view(), name="atualiza_services"),

    # Para deletar o objeto, o procedimento é parecido com o de atualização.
    # GET/POST /services (services está definido em url.py petshop)/excluir/{pk do objeto}
    path('excluir/<pk>', ServicesDeleteView.as_view(), name="deleta_services"),
]
