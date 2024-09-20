from django.db import models
from equipos.models import Teams
from posiciones.models import Positions

class Players(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='fotos_jugadores/')
    fecha_nacimiento = models.DateField()
    posicion = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True)
    numero_camiseta = models.IntegerField()
    titular = models.BooleanField(default=False)
    equipo = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Meta:
    verbose_name = "Player"
    verbose_name_plural = "Players"
    db_table = "player"
    ordering = ['id']
# Create your models here.
