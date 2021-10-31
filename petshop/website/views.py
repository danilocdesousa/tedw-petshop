from petshop.models import Clientes
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from website.forms import InsereClientesForm

# Utilizando a TemplateView para rederização da página.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"
    
# Utilizando a ListView para a listagem de clientes.
class ClientesListView(ListView):
    template_name = "website/lista.html"
    model = Clientes
    context_object_name = 'clientes'
    
# Utilizando a CreateView para adicionar um novo cliente.
class ClientesCreateView (CreateView):
    template_name = "website/cria.html"
    model = Clientes
    form_class = InsereClientesForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um cliente, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("website:lista_clientes")
    
# Utilizando a UpdateView para a atualização de clientes.
class ClientesUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Clientes
    fields = '__all__' # fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']
    context_object_name = 'clientes'
    success_url = reverse_lazy("website:lista_clientes")

# Utilizando a DeleteView para deletar um cliente.
class ClientesDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Clientes
    context_object_name = 'clientes'
    success_url = reverse_lazy("website:lista_clientes")
