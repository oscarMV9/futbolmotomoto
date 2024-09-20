from django.shortcuts import render, get_object_or_404
from .models import Teams
from categorias.models import Continente

def list_groups(request, id_continente):
    continente = get_object_or_404(Continente, id=id_continente)
    teams = Teams.objects.filter(continente=continente)
    return render(request, 'equipos/equipos.html', {'teams': teams, 'continente': continente})


# Create your views here.
