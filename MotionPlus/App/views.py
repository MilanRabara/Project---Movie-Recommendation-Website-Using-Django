from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'index.html')


def login(request):
    return render(request,'registration/login.html')


def page(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == "POST":
        try:
            username=request.POST.get('username1', False)
            email=request.POST.get('email1', False)
            password=request.POST.get('password1', False)
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        except:
            return render(request,'registration/login.html')
    return render(request,'registration/login.html')
