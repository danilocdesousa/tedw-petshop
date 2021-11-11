from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from petshop.models import Clientes
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from website.forms import InsereClientesForm


# Impedir acesso se não estiver logado.
@method_decorator(login_required, name='dispatch')
# Utilizando a TemplateView para rederização da página.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


@method_decorator(login_required, name='dispatch')
# Utilizando a ListView para a listagem de clientes.
class ClientesListView(ListView):
    template_name = "website/lista.html"
    model = Clientes
    context_object_name = 'clientes'


@method_decorator(login_required, name='dispatch')
# Utilizando a CreateView para adicionar um novo cliente.
class ClientesCreateView (CreateView):
    template_name = "website/cria.html"
    model = Clientes
    form_class = InsereClientesForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um cliente, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("website:lista_clientes")


@method_decorator(login_required, name='dispatch')
# Utilizando a UpdateView para a atualização de clientes.
class ClientesUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Clientes
    # fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']
    fields = '__all__'
    context_object_name = 'clientes'
    success_url = reverse_lazy("website:lista_clientes")


@method_decorator(login_required, name='dispatch')
# Utilizando a DeleteView para deletar um cliente.
class ClientesDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Clientes
    context_object_name = 'clientes'
    success_url = reverse_lazy("website:lista_clientes")
