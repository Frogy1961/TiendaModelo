from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage, send_mail
from decouple import config

# Create your views here.


def contact(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de H&B Shop",
            "De {} con email {} enía el siguiente mensaje:\n\n {}".format(nombre,email,contenido),"",
            [config('EMAIL_HOST_USER')],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")

    return render(request, "contacto/contacto.html", {'MiFormulario':formulario_contacto})