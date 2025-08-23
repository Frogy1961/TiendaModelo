from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),  # Tienda completa
    path('categoria/<int:categoria_id>/', views.tienda, name='tienda_categoria'),  # Filtrar por categoría
]
