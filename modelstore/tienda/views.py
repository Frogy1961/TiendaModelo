from django.shortcuts import render, get_object_or_404
from .models import Producto, CategoriaProd

def tienda(request, categoria_id=None):
    # Todas las categorías activas
    categorias = CategoriaProd.objects.filter(status=True)

    # Todos los productos por defecto
    productos = Producto.objects.all()
    categoria_activa = None

    # Si hay categoría seleccionada, filtramos productos
    if categoria_id:
        categoria = get_object_or_404(CategoriaProd, id=categoria_id)
        productos = productos.filter(categoria=categoria)
        categoria_activa = categoria.id

    return render(request, "tienda.html", {
        "categorias": categorias,
        "productos": productos,
        "categoria_activa": categoria_activa
    })


