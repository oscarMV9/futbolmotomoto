from django.db import models

CONT_ROLE = [
    ('suramerica', 'suramerica'),
    ('centroamerica', 'centroamerica'),
    ('norteamerica', 'norteamerica'),
    ('europa', 'europa'),
    ('africa', 'africa'),
    ('medio oriente', 'medio oriente'),
    ('oseania','oseania')
]

class Continente(models.Model):
    nombre = models.CharField(max_length=40, choices=CONT_ROLE)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Meta:
    verbose_name = "Continent"
    verbose_name_plural = "Continents"
    db_table = "continent"
    ordering = ['id']


# Create your models here.
