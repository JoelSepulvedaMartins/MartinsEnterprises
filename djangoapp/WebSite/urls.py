from django.contrib import admin
from django.urls import path
from WebSite.views import index, aboutClient, contact, booking, service,error404 ,team, testimonial, nossos_servicos
from WebSite import views

app_name = 'WebSite'
urlpatterns = [

    # WebSite:index   WebSite:servicosAdmin .....   url reverse, como buscar
    path('', index, name='index'),
    path('aboutClient/', aboutClient, name='aboutClient'),
    path('error404/', error404, name='404'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('nossos_servicos/', nossos_servicos, name='nossos_servicos'),    


]
