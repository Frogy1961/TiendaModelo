from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "website/Home.html")







