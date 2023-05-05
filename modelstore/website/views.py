from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def home(request):

    return render(request, "website/Home.html")


def services(request):

    servicios=Servicio.objects.all()

    return render(request, "website/Servicios.html", {"servicios" : servicios})


def store(request):
    return render(request, "website/Tienda.html")


def blog(request):
    return render(request, "website/Blog.html")


def contact(request):
    return render(request, "website/Contacto.html")

