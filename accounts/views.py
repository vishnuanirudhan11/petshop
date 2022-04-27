from django.shortcuts import render,redirect
from django.contrib import messages
from.models import user
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('myapp:petshop')
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('myapp:petshop')
        else:
            messages.info(request, 'invalid details')
            a = 'invalid details'
            return render(request, 'login.html', {'k': a})
    a=''
    return render(request, 'login.html', {'k':a})

def reg(request,k=''):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2 = request.POST.get('password2')
        birthday=request.POST.get('birthday')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        if password1 != password2:
            a='password is not matching'
            return render(request, 'reg.html', {'k': a})
        elif User.objects.filter(username=username).exists():
            a="username already exist"
            return render(request,'reg.html',{'k':a})
        elif User.objects.filter(email=email).exists():
            a='email id is already exist'
            return render(request,'reg.html',{'k':a})
        else:
            s=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,
                   email=email)
            s.save()
        return redirect('login')

    return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('login')