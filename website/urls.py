from django import views
from django.contrib import admin
from django.urls import path
from .import views

apps_name = 'website'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home")
]
