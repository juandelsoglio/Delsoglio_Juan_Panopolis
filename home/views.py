from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador, Club, Descripcion
from .forms import JugadorForm, ClubForm, DescripcionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# PÁGINAS PRINCIPALES 

def inicio(request):
    return render(request, 'home/index.html')

def acerca(request):
    return render(request, 'home/acerca.html')

@login_required
def carga(request):
    return render(request, 'home/cargar.html')

@login_required
def listado(request):
    query = request.GET.get('nombre')
    if query:
        jugadores = Jugador.objects.filter(nombre__icontains=query)
    else:
        jugadores = Jugador.objects.all()
    return render(request, 'home/listado.html', {'jugadores': jugadores, 'query': query})

# CARGAR 

@login_required
def cargar_jugador(request):
    mensaje = ""
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = "🏃⚽ El jugador ha sido cargado correctamente"
            form = JugadorForm()
    else:
        form = JugadorForm()
    return render(request, 'home/cargar_jugador.html', {'form': form, 'mensaje': mensaje})

@login_required
def cargar_club(request):
    mensaje = ""
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            mensaje = "🏳️ El club ha sido cargado correctamente"
            form = ClubForm()
    else:
        form = ClubForm()
    return render(request, 'home/cargar_club.html', {'form': form, 'mensaje': mensaje})



@login_required
def cargar_descripcion(request):
    mensaje = ""
    if request.method == 'POST':
        form = DescripcionForm(request.POST, user=request.user)
        if form.is_valid():
            descripcion = form.save(commit=False)
            descripcion.usuario = request.user.username  
            descripcion.save()
            mensaje = "💬 La descripción del jugador ha sido cargada correctamente"
            form = DescripcionForm(user=request.user)
    else:
        form = DescripcionForm(user=request.user)

    return render(request, 'home/cargar_descripcion.html', {'form': form, 'mensaje': mensaje})


# DETALLES 

@login_required
def detalle_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    descripcion = Descripcion.objects.filter(jugador=jugador)
    return render(request, 'home/detalle_jugador.html', {'jugador': jugador, 'descripcion': descripcion})

#  ELIMINAR 

@login_required
def eliminar(request):
    return render(request, 'home/eliminar.html')

@login_required
def eliminar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, 'home/eliminar_jugador.html', {'jugadores': jugadores})

class EliminarJugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = 'home/confirmar_eliminacion_jugador.html'
    success_url = reverse_lazy('home:eliminar_jugador')

@login_required
def eliminar_club(request):
    clubes = Club.objects.all()
    return render(request, 'home/eliminar_club.html', {'clubes': clubes})

class EliminarClub(LoginRequiredMixin, DeleteView):
    model = Club
    template_name = 'home/confirmar_eliminacion_club.html'
    success_url = reverse_lazy('home:eliminar_club')

@login_required
def eliminar_descripcion(request):
    descripciones = Descripcion.objects.all()
    return render(request, 'home/eliminar_descripcion.html', {'descripciones': descripciones})

class EliminarDescripcion(LoginRequiredMixin, DeleteView):
    model = Descripcion
    template_name = 'home/confirmar_eliminacion_descripcion.html'
    success_url = reverse_lazy('home:eliminar_descripcion')

#  ACTUALIZAR 

@login_required
def actualizar(request):
    return render(request, 'home/actualizar.html')

@login_required
def actualizar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, 'home/actualizar_jugador.html', {'jugadores': jugadores})

@login_required
def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    form = JugadorForm(request.POST or None, request.FILES or None, instance=jugador)
    if form.is_valid():
        form.save()
        return redirect('home:actualizar_jugador')
    return render(request, 'home/editar_jugador.html', {'form': form})

@login_required
def actualizar_club(request):
    clubes = Club.objects.all()
    return render(request, 'home/actualizar_club.html', {'clubes': clubes})

@login_required
def editar_club(request, id):
    club = get_object_or_404(Club, id=id)
    form = ClubForm(request.POST or None, instance=club)
    if form.is_valid():
        form.save()
        return redirect('home:actualizar_club')
    return render(request, 'home/editar_club.html', {'form': form})

@login_required
def actualizar_descripcion(request):
    descripciones = Descripcion.objects.all()
    return render(request, 'home/actualizar_descripcion.html', {'descripciones': descripciones})

@login_required
def editar_descripcion(request, id):
    descripcion = get_object_or_404(Descripcion, id=id)
    form = DescripcionForm(request.POST or None, instance=descripcion)
    if form.is_valid():
        form.save()
        return redirect('home:actualizar_descripcion')
    return render(request, 'home/editar_descripcion.html', {'form': form})


