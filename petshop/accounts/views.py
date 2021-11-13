from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

# Create your views here.

class SignUpView(generic.CreateView): 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'tedw-petshop/website/templates/registration/register.html'