# Importação das funções definidas no arquivo views.py.
from django.urls import path
from accounts.views import SignUpView

app_name = 'accounts'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /cadastrar
    path('register/', SignUpView.as_view, name="signup"),
]
