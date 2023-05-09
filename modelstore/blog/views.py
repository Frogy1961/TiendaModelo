from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):

    posts=Post.objects.all()

    return render(request, "blog/Blog.html", {"posts" : posts})
