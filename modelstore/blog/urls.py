from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
]



