from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name="home"),
 path('contact.html', views.contact, name="contact"),
 path('about.html', views.about, name="about"),
 path('gallery.html', views.gallery, name="gallery"),
 path('blog.html', views.blog, name="blog"),
]

