from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario


# ----------- FORMULARIO DE REGISTRO -----------
class FormularioRegistro(UserCreationForm):
    username = forms.CharField(required=True, label="Nombre de usuario")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    edad = forms.IntegerField(required=False, label="Edad")
    hinchade = forms.CharField(required=False, max_length=50, label="Hincha de")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False, label="Avatar")

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email','edad','hinchade', 'avatar','password1', 'password2']
        # Esto elimina los mensajes de ayuda automáticos
        help_texts = {field: '' for field in fields}


# ----------- FORMULARIO DE EDICIÓN DE USUARIO -----------
class FormularioEdicionUsuario(UserChangeForm):
    password = None 
    username = forms.CharField(required=True, label="Nombre de usuario", disabled=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    edad = forms.IntegerField(required=False, label="Edad")
    hinchade = forms.CharField(required=False, max_length=50, label="Hincha de")
    avatar = forms.ImageField(required=False, label="Avatar")

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'edad', 'hinchade', 'avatar'
        ]
        help_texts = {field: '' for field in fields}



