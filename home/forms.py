from django import forms
from .models import Club, Jugador, Descripcion

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nombre', 'provincia', 'fundacion', 'escudo']  

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'club', 'foto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].queryset = Club.objects.all()
        self.fields['club'].empty_label = "Seleccione un club"

class DescripcionForm(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = ['usuario', 'jugador', 'texto']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['usuario'].initial = user.username
            self.fields['usuario'].disabled = True
            self.fields['usuario'].label = f"Usuario: {user.username}"

        self.fields['jugador'].queryset = Jugador.objects.all()
        self.fields['jugador'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido}"



