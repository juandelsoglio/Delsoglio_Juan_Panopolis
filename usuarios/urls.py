
from django.urls import path
from . import views
from .views import EditarContrasenia 

app_name = "usuarios"

urlpatterns = [
  
    path('login/', views.login_view, name='login'),
  
    path('registro/', views.registro_view, name='registro'),

    path('logout/', views.logout_view, name='logout'),

    path('detalle/', views.detalle_usuario, name='detalle'),

    path('editar/', views.editar_usuario, name='editar'),

    path('cambiar-contrasena/', EditarContrasenia.as_view(), name='editar-contrasena'),
]
