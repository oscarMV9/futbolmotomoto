from django.contrib import admin
from django.urls import path, include
from .views import index,home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('categorias/', include('categorias.urls')),
    path('equipos/', include('equipos.urls')),
    path('jugadores/', include('jugadores.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
