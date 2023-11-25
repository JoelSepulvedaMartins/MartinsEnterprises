from django.contrib import admin
from django.urls import path
from WebSite.views import index, nossos_servicos,servicosAdmin,see_service,serviceDelete
from WebSite import views

app_name = 'WebSite'
urlpatterns = [
    # WebSite:index   WebSite:servicosAdmin .....   url reverse, como buscar
    path('', index, name='index'),
    path('nossos_servicos/', nossos_servicos,name='nossos_servicos'), # type: ignore
    path('servicosAdmin/', servicosAdmin, name='servicosAdmin'), # type: ignore
    path('see_service/<int:id>', see_service, name='see_service'), # type: ignore , recebendo parametro na url
    path('serviceDelete/<int:id>', serviceDelete, name='serviceDelete'),
]
