from petshop.models import Services
from django.views.generic import CreateView
from django.urls import reverse_lazy
from services.forms import InsereServicesForm

# Utilizando a CreateView para adicionar um novo serviço.


class ServicesCreateView(CreateView):
    template_name = "services/cria.html"
    model = Services
    form_class = InsereServicesForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um serviço, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("services:lista_services")
