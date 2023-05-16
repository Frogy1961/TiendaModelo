from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):

    posts=Post.objects.all()

    return render(request, "blog/Blog.html", {"posts" : posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    post=Post.objects.filter(categorias=categoria)
    return render(request, "Blog/Categorias.html", {'categoria' : categoria, "posts" : post})

def post(request, post_id):
    titulo=Post.objects.get(id=post_id)
    posts=Post.objects.filter(titulo=titulo) 
    return render(request,"Blog/Post.html", {'titulo' : titulo, "posts" : posts})

