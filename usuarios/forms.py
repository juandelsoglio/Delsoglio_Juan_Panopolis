from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    edad = forms.IntegerField(label='Edad', required=False)
    telefono = forms.CharField(label='Número de teléfono', required=False) 
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'edad', 'email', 'telefono', 'password1', 'password2']
        help_texts = { llave: '' for llave in fields}


class FormularioEdicionUsuario(UserChangeForm):
    password = None

    username = forms.CharField(label='Nombre de usuario', required=False, disabled=True)
    email = forms.EmailField(label='Correo electrónico', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    edad = forms.IntegerField(label='Edad', required=False)
    telefono = forms.CharField(label='Número de teléfono', required=False) 
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono']
        help_texts = { llave: '' for llave in fields }


