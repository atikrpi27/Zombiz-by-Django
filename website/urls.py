from django import views
from django.urls import path
from .import views

apps_name = 'website'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('project/', views.project, name="project"),
    path('team/', views.team, name="team"),
    path('blog/', views.blog, name="blog"),
    path('blog-single/', views.blogSingle, name="blogSingle"),
    path('contact/', views.contact, name="contact"),
   
]
