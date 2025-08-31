from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('detalle/', views.detalle_usuario, name='detalle'),
    path('detalle/editar', views.editar_usuario, name='editar'),
    path('detalle/contrasenia', views.EditarContrasenia.as_view(), name='editar_contrasenia'),
]
