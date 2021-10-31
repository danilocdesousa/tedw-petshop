from registration.models import Clientes
from django.views.generic import TemplateView, ListView, UpdateView
from django.urls import reverse_lazy


# Utilizando a TemplateView para rederização da página.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"
    
# Utilizando a ListView para a listagem de clientes.
class ClientesListView(ListView):
    template_name = "website/lista.html"
    model = Clientes
    context_object_name = 'clientes'
    
# Utilizando a UpdateView para a atualização de clientes.
class ClientesUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Clientes
    fields = '__all__' # fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']
    context_object_name = 'clientes'
    success_url = reverse_lazy("website:lista_clientes")
