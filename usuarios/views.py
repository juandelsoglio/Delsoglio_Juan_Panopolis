from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from usuarios.forms import FormularioRegistro, FormularioEdicionUsuario
from usuarios.models import PerfilUsuario

def login_view(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            django_login(request, user)
            
            return redirect('panopolis:inicio')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'formulario': formulario})


def registro_view(request):
    if request.method == 'POST':
        # El formulario de registro debe ser capaz de manejar archivos,
        # por eso se le pasan request.FILES
        formulario = FormularioRegistro(request.POST, request.FILES)
        if formulario.is_valid():
            # Guarda los campos del modelo User
            user = formulario.save()
            
            # Obtiene los datos del formulario que no son del modelo User
            edad = formulario.cleaned_data.get('edad')
            telefono = formulario.cleaned_data.get('telefono')
            avatar = formulario.cleaned_data.get('avatar')
            
            # Crea el perfil de usuario y lo asocia con el usuario recién creado
            PerfilUsuario.objects.create(
                user=user,
                edad=edad,
                telefono=telefono,
                avatar=avatar
            )
            
            return redirect('panopolis:inicio')
    else:
        formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def logout_view(request):
    """
    Vista para cerrar la sesión del usuario.
    """
    django_logout(request)
    return redirect('panopolis:inicio')

@login_required
def detalle_usuario(request):
    # Se obtienen o crean el perfil del usuario para asegurar su existencia
    perfil, creado = PerfilUsuario.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/detalle.html', {
        'usuario': request.user,
        'perfil': perfil
    })
    
@login_required
def editar_usuario(request):
    perfil = request.user.perfilusuario
    
    if request.method == 'POST':
        # Al igual que en registro, el formulario de edición debe manejar archivos
        formulario = FormularioEdicionUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            # Guarda los cambios en el modelo User
            usuario = formulario.save()
            
            # Actualiza los campos del perfil
            perfil.edad = formulario.cleaned_data.get('edad')
            perfil.telefono = formulario.cleaned_data.get('telefono')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            # Si se subió un nuevo avatar, se actualiza
            if nuevo_avatar:
                perfil.avatar = nuevo_avatar
            
            perfil.save()
            return redirect('usuarios:detalle')
    else:
        # Se inicializa el formulario con los datos del usuario para mostrarlos
        datos_iniciales = {
            'edad': perfil.edad,
            'telefono': perfil.telefono,
            'avatar': perfil.avatar
        }
        formulario = FormularioEdicionUsuario(instance=request.user, initial=datos_iniciales)

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('usuarios:detalle')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.help_text = None
        return form
