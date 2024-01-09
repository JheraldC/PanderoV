from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicio(request):
    return render(request, 'servicio.html')

def contacto(request):
    return render(request, 'contacto.html')