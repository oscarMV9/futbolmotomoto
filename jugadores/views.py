from django.shortcuts import render, get_object_or_404
from equipos.models import Teams
from .models import Players

def listado_equipos(request):
    equipos = Teams.objects.all()
    return render (request, 'jugadores/listado_equipos.html', {'equipos': equipos})

def player_list(request, id_equipos):
    equipo = get_object_or_404(Teams, id=id_equipos)
    player = Players.objects.filter(equipo=equipo)
    return render(request, 'jugadores/jugadores.html', {'equipo': equipo, 'player': player})

# Create your views here.
