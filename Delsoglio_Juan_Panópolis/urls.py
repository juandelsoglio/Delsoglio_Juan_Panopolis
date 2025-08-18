"""
URL configuration for Delsoglio_Juan_Panópolis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las URLs de la app panopolis y le asignamos un namespace.
    path('', include('panopolis.urls', namespace='panopolis')),
    # Incluimos las URLs de la app usuarios y le asignamos su propio namespace.
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
]
