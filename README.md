## tedw-petshop

### Para rodar o projeto

Instalar o django:
```
pip install django
```
Instalar o django-widget-tweaks:
```
pip install django-widget-tweaks
```

Instalar o django-crispy-forms:
```
pip install django-crispy-forms
```

Criar as Migrações:
```
python manage.py makemigrations petshop
```

Efetivar as Migrações no banco de dados:
```
python manage.py migrate
```

Executar o servidor de testes do Django:
```
python manage.py runserver
```

Por fim, acessar o seu navegador na página http://localhost:8000 (por padrão).
