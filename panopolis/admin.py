from django.contrib import admin
from .models import Paciente, Estudio, Resultado

admin.site.register(Paciente)
admin.site.register(Estudio)
admin.site.register(Resultado)

