from django.contrib import admin
from django.urls import path
from WebSite.views import index, nossos_servicos,servicosAdmin


app_name = 'WebSite'
urlpatterns = [
    # WebSite:index    url reverse, como buscar
    path('', index, name='index'),
    path('nossos_servicos', nossos_servicos),
    path('servicosAdmin', servicosAdmin),
]
