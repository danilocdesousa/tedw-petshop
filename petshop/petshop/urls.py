from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # Interface administrativa.
    path('admin/', admin.site.urls),

    # Inclui as URLs do app 'website'.
    path('', include('website.urls', namespace='website')),

    # Inclui as URLs do app 'services'.
    path('services/', include('services.urls', namespace='services')),

    # Inclui as URLs do app 'pets'.
    path('pets/', include('pets.urls', namespace='pets')),

    #Inclui as URLs de 'login'
    path('accounts/', include('django.contrib.auth.urls')),
]
