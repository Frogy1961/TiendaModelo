from django.shortcuts import render
from .models import Producto, CategoriaProd

# Create your views here.

def store(request):

    productos = Producto.objects.all()

    return render(request, "Tienda/Tienda.html", {"productos":productos})

