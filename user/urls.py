from django.urls import path
from .import views

apps_name = 'user'

urlpatterns = [
    path('registrarion/', views.reg, name='reg'),
    path('login/', views.login, name='login'),
]