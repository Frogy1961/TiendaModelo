from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('services', views.services, name='servicios'),
    path('store', views.store, name='tienda'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contacto'),
]

