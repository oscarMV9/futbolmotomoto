from django.shortcuts import render, get_object_or_404
from .models import Continente

def listado_continentes(request):
    continentes = Continente.objects.all()
    return render(request, 'categorias/listado_continentes.html', {'continentes': continentes})

# Create your views here.
