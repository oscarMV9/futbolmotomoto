from django.db import models
from categorias.models import Continente

class Teams(models.Model):
    nombre = models.CharField(max_length=50)
    bandera = models.ImageField(upload_to='banderas/')
    escudo = models.ImageField(upload_to='escudos/')
    continente = models.ForeignKey(Continente, related_name='equipos', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        db_table = "team"
        ordering = ['id']
# Create your models here.
