from django.contrib import admin
from .models import Continente

admin.site.register(Continente)

class categoriasAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

# Register your models here.
