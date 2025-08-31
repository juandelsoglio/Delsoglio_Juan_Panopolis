from django.db import models

class Club(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    fundacion = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    posicion = models.CharField(max_length=50, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return self.apellido

class Descripcion(models.Model):
    usuario = models.CharField(max_length=100)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Descripción de {self.jugador.nombre}{self.jugador.apellido}"

