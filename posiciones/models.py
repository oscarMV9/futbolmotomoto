from django.db import models

class Positions(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre
    
class Meta:
    verbose_name = "Posicion"
    verbose_name_plural = "Posiciones"
    db_table = "posicion"
    ordering = ['id']

# Create your models here.
