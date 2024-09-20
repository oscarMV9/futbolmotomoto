from django.db import models

class Tecnic(models.Model):
    ROLE_CHOISES = [
        ('tecnico', 'tecnico'),
        ('asistente', 'asistente'),
        ('medico', 'medico'),
        ('preparador fisico', 'preparador fisico'),
    ]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30)
    rol = models.CharField(max_length=40, choices=ROLE_CHOISES)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.rol}'
    
class Meta:
    verbose_name = "Tecnic"
    verbose_name_plural = "Tecnics"
    db_table = "tecnic"
    ordering = ['id']

# Create your models here.
