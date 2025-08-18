from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"

class Estudio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Resultado(models.Model):
    
    titulo = models.CharField(max_length=255, verbose_name="Título del Informe")
    subtitulo = models.CharField(max_length=255, verbose_name="Subtítulo")
    cuerpo = models.TextField(verbose_name="Cuerpo del Informe")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='resultados', null=True)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='resultados')
    
    
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='resultados_subidos', verbose_name="Autor (Personal de laboratorio)")
    
    
    imagen = models.ImageField(upload_to='informes_imagenes/', blank=True, null=True, verbose_name="Imagen/Archivo adjunto")

    def __str__(self):
        return f"Resultado de {self.estudio.nombre} para {self.paciente}"
