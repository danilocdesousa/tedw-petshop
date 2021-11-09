# Importação das funções definidas no arquivo views.py.
from django.urls import path
from pets.views import PetsCreateView, PetsListView, PetsUpdateView, PetDeleteView

app_name = 'pets'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('cadastrar/', PetsCreateView.as_view(), name="cadastra_pets"),

    # GET /listar
    path('listar/', PetsListView.as_view(), name="lista_pets"),

    # Para atualizar o objeto, devemos buscá-lo via 'id' ou 'slug'. Também pode ser atualizado através do método get_object().
    # GET/POST /pets (pets está definido em url.py petshop)/{pk do objeto}
    path('<pk>', PetsUpdateView.as_view(), name="atualiza_pets"),

    # Para deletar o objeto, o procedimento é parecido com o de atualização.
    # GET/POST /pets (pets está definido em url.py petshop)/excluir/{pk do objeto}
    path('excluir/<pk>', PetDeleteView.as_view(), name="deleta_pets"),
]
