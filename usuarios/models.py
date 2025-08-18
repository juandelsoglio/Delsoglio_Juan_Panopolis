from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class PerfilUsuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField(null=True, blank=True)
    area_interes = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares',blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'