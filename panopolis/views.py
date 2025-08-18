from django.shortcuts import render


def inicio(request):
    """Vista para la página de inicio"""
    return render(request, 'panopolis/index.html')

def about(request):
    """Vista para la página 'Acerca de Mí'"""
    return render(request, 'panopolis/about.html')