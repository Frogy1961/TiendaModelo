from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages

# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido


        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido
        nombreusuario=request.username,
        emailusuario=request.usermail
        )

    messages.success(request, "El pedido de ha creado existosamente")

    return redirect("../tienda")
