"""
URL configuration for panopolis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from home.views import EliminarJugador, EliminarDescripcion, EliminarClub

app_name = 'home'

urlpatterns = [
    # Páginas estáticas
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('cargar/', views.carga, name='cargar'),
    path('listado/', views.listado, name='listado'),
    
    # Cargar datos
    path('jugador/cargar/', views.cargar_jugador, name='cargar_jugador'),
    path('club/cargar/', views.cargar_club, name='cargar_club'),
    path('descripcion/cargar/', views.cargar_descripcion, name='cargar_descripcion'),

    # Detalles
    path('jugador/<int:id>/', views.detalle_jugador, name='detalle_jugador'),

    # Eliminar
    path('eliminar/', views.eliminar, name='eliminar'),

    path('eliminar/jugador/', views.eliminar_jugador, name='eliminar_jugador'),
    path('eliminar/jugador/<int:pk>/', EliminarJugador.as_view(), name='eliminar_jugador_confirm'),

    path('eliminar/club/', views.eliminar_club, name='eliminar_club'),
    path('eliminar/club/<int:pk>/', EliminarClub.as_view(), name='eliminar_club_confirm'),

    path('eliminar/descripcion/', views.eliminar_descripcion, name='eliminar_descripcion'),
    path('eliminar/descripcion/<int:pk>/', EliminarDescripcion.as_view(), name='eliminar_descripcion_confirm'),

    # Actualizar
    path('actualizar/', views.actualizar, name='actualizar'),

    path('actualizar/jugador/', views.actualizar_jugador, name='actualizar_jugador'),
    path('editar/jugador/<int:id>/', views.editar_jugador, name='editar_jugador'),

    path('actualizar/club/', views.actualizar_club, name='actualizar_club'),
    path('editar/club/<int:id>/', views.editar_club, name='editar_club'),
    
    path('actualizar/descripcion/', views.actualizar_descripcion, name='actualizar_descripcion'),
    path('editar/descripcion/<int:id>/', views.editar_descripcion, name='editar_descripcion'),
]
