from django.shortcuts import render
from user.models import Registration

# Create your views here.
def reg(request):
    return render(request, 'reg.html')

def login(request):
    return render(request, 'login.html')