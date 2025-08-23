from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.procesar_pedido, name='procesar_pedido'),
    path('<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
   
]