from django.urls import path
from . import views
from .views import player_list

urlpatterns = [
    path('/jugadores', views.listado_equipos, name='listado_equipos'),
    path('players/<int:id_equipos>', player_list, name='player_list'),
]