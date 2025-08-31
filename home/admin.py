from django.contrib import admin
from .models import Jugador, Club, Descripcion

admin.site.register(Jugador)
admin.site.register(Descripcion)
admin.site.register(Club)