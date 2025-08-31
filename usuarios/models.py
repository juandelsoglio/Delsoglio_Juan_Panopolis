from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField(null=True, blank=True)
    hinchade = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
