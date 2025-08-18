from django import forms
from .models import Paciente, Estudio, Resultado

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'email']

class EstudioForm(forms.ModelForm):
    class Meta:
        model = Estudio
        fields = ['nombre', 'descripcion']

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado   
        fields = ['titulo', 'subtitulo', 'cuerpo', 'paciente', 'estudio', 'autor', 'imagen']



