from django.shortcuts import redirect, render
from user.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        uname = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        district = request.POST.get('district')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        gender = request.POST.get('gender')

        if password == c_password:
            # for create user in User table from Registration HTML Form.
            user = User.objects.create_user(first_name = fname, last_name = lname, username = uname , email = email)
            user.set_password(password)
            user.save()

            # for save data in database Registration Table from Registration HTML Form.
            reg = Registration(first_name = fname, last_name = lname, username = uname, phone = phone, email = email, district = district, password = password, c_password = c_password, gender = gender)
            reg.save()
            return redirect('login')          
        
        else:
            messages.info(request,'Password and confirm password does not match')
            
    return render(request, 'reg.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password Invalid.")

    return render(request, 'login.html')