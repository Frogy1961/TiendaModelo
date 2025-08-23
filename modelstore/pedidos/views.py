from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

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
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        )

    messages.success(request, "El pedido de ha creado existosamente")
    
    return redirect("detalle_pedido", pedido_id=pedido.id)

@login_required(login_url="/autenticacion/logear")
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    lineas = pedido.lineapedido_set.all()

    return render(request, "pedido/detalle_pedido.html", {
        "pedido": pedido,
        "lineas": lineas
    })

def enviar_mail(**kwargs):

    asunto="Gracias por tu pedido"
    mensaje=render_to_string("emails/pedido.html", {
         "pedido": kwargs.get("pedido"),
         "lineas_pedido": kwargs.get("lineas_pedido"),
         "nombreusuario": kwargs.get("nombreusuario")
        



    })

    mensaje_texto=strip_tags(mensaje)
    from_email="home.bussines.shop@gmail.com"
    to=kwargs.get("email_usuario")

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)