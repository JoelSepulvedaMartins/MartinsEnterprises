from django.contrib import admin
from django.urls import path
from WebSite.views import index

app_name = 'WebSite'
urlpatterns = [
    # WebSite:index    url reverse, como buscar
    path('', index, name='index'),
]
