from django.urls import path
from . import views

urlpatterns = [
    path('/categorias', views.listado_continentes, name='listado_continentes'),
]