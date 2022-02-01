from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
    
def service(request):
    return render(request,"service.html")

def project(request):
    return render(request,"project.html")

def team(request):
    return render(request,"team.html")

def blog(request):
    return render(request,"blog.html")

def blogSingle(request):
    return render(request,"blog_single.html")

def contact(request):
    return render(request,"contact.html")

