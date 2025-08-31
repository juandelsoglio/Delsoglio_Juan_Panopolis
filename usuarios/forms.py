from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

# ----------- FORMULARIO DE REGISTRO -----------
class FormularioRegistro(UserCreationForm):
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(required=False)
    hinchade = forms.CharField(required=False, max_length=50, label="Hincha de")
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'edad', 'hinchade', 'avatar']

# ----------- FORMULARIO DE EDICIÓN DE USUARIO -----------
class FormularioEdicionUsuario(UserChangeForm):
    password = None  # Oculta el campo contraseña
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True)
    edad = forms.IntegerField(required=False)
    hinchade = forms.CharField(required=False, max_length=50, label="Hincha de")
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'edad', 'hinchade', 'avatar']
