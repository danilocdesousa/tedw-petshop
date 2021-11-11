## tedw-petshop

### Para rodar o projeto

Instalar as dependências:
```
pip install -r requirements.txt
```

Criar as Migrações:
```
python manage.py makemigrations
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
