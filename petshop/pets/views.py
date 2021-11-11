from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from petshop.models import Pet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pets.forms import InserePetsForm


# Impedir acesso se não estiver logado.
@method_decorator(login_required, name='dispatch')
# Utilizando a CreateView para adicionar um novo pet.
class PetsCreateView(CreateView):
    template_name = "pets/cria.html"
    model = Pet
    form_class = InserePetsForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um pet, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("pets:lista_pets")


@method_decorator(login_required, name='dispatch')
# Utilizando a ListView para a listagem de pets.
class PetsListView(ListView):
    template_name = "pets/lista.html"
    model = Pet
    context_object_name = 'pets'


@method_decorator(login_required, name='dispatch')
# Utilizando a UpdateView para a atualização de pets.
class PetsUpdateView(UpdateView):
    template_name = "pets/atualiza.html"
    model = Pet
    # fields = ['nome', 'especie', 'raca', 'sexo', 'notas', 'cliente']
    fields = '__all__'
    context_object_name = 'pets'
    success_url = reverse_lazy("pets:lista_pets")


@method_decorator(login_required, name='dispatch')
# Utilizando a DeleteView para deletar um pet.
class PetsDeleteView(DeleteView):
    template_name = "pets/exclui.html"
    model = Pet
    context_object_name = 'pets'
    success_url = reverse_lazy("pets:lista_pets")
