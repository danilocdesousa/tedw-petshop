# Importação das funções definidas no arquivo views.py.
from django.urls import path
from . import views

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # Criar a url register/
    path('register/', views.SignUp.as_view(), name="signup"),
]
