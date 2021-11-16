from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from petshop.models import Sales
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from sales.forms import InsereSalesForm


# Impedir acesso se não estiver logado.
@method_decorator(login_required, name='dispatch')
# Utilizando a CreateView para adicionar uma nova venda.
class SalesCreateView(CreateView):
    template_name = "sales/cria.html"
    model = Sales
    form_class = InsereSalesForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar uma venda, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("sales:lista_sales")


@method_decorator(login_required, name='dispatch')
# Utilizando a ListView para a listagem de vendas.
class SalesListView(ListView):
    template_name = "sales/lista.html"
    model = Sales
    context_object_name = 'sales'

@method_decorator(login_required, name='dispatch')
# Utilizando a UpdateView para a atualização de vendas.
class SalesUpdateView(UpdateView):
    template_name = "sales/atualiza.html"
    model = Sales
    # fields = ['cliente', 'pet', 'servico', 'preco', 'data']
    fields = '__all__'
    context_object_name = 'sales'
    success_url = reverse_lazy("sales:lista_sales")

@method_decorator(login_required, name='dispatch')
# Utilizando a DeleteView para deletar uma venda.
class SalesDeleteView(DeleteView):
    template_name = "sales/exclui.html"
    model = Sales
    context_object_name = 'sales'
    success_url = reverse_lazy("sales:lista_sales")
