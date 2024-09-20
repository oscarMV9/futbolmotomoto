from django.urls import path
from . import views

urlpatterns = [
    path('continente/<int:id_continente>/', views.list_groups, name='equipos_por_continente'),
]