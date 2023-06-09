from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=250)
    imagen = models.ImageField(upload_to='Servicios', blank=False, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'

    def __str__(self):
        return self.titulo

        