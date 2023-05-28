from django.db import models

# Create your models here

class CategoriaProd(models.Model):

    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="Tienda",blank=True,null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status =  models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    class Meta:
        verbose_name='CategoriaProd'
        verbose_name_plural='CategoriasProd'

    def __str__ (self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="Tienda",blank=True, null=True)
    imagen2 = models.ImageField(upload_to="Tienda", blank=True, null=True)
    imagen3 = models.ImageField(upload_to="Tienda", blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    categoria = models.ManyToManyField(CategoriaProd)
    precio = models.FloatField(max_length=20)
    precio_oferta = models.FloatField(max_length=20)
    created = models.BooleanField(default=True)
    updated = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
    
    
