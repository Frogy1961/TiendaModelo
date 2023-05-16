from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='Nombre',required=True ,max_length=100)
    email = forms.CharField(label='email', required=True, max_length=30)
    contenido = forms.CharField(label='Contenido', max_length=100, widget=forms.Textarea)

