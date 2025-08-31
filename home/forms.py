from django import forms
from .models import Club, Jugador, Descripcion

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nombre', 'provincia', 'fundacion']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'club', 'foto']

class DescripcionForm(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = ['usuario', 'jugador', 'texto']
