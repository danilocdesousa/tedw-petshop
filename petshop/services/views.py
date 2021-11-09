from petshop.models import Services
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from services.forms import InsereServicesForm


# Utilizando a CreateView para adicionar um novo serviço.
class ServicesCreateView(CreateView):
    template_name = "services/cria.html"
    model = Services
    form_class = InsereServicesForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um serviço, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("services:lista_services")


# Utilizando a ListView para a listagem de serviços.
class ServicesListView(ListView):
    template_name = "services/lista.html"
    model = Services
    context_object_name = 'services'


# Utilizando a UpdateView para a atualização de serviços.
class ServicesUpdateView(UpdateView):
    template_name = "services/atualiza.html"
    model = Services
    fields = '__all__'  # fields = ['nome', 'preco']
    context_object_name = 'services'
    success_url = reverse_lazy("services:lista_services")


# Utilizando a DeleteView para deletar um serviço.
class ServicesDeleteView(DeleteView):
    template_name = "services/exclui.html"
    model = Services()
    context_object_name = 'services'
    success_url = reverse_lazy("services:lista_services")
