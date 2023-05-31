from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def homepage(request):
    context_user={}
    return render(request,'home.html',context_user )

def login(request):
    if request.method =='POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # print("username::",username,"password::",password)
        user = authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            print("not user find")
    context_user={}
    return render(request,'login.html',context_user )


def logout(request):
    auth_logout(request)
    return redirect('login')

def dogs(request):
    context_user={}
    return render(request,'dogs.html',context_user )

def trainedgerman(request):
    context_user={}
    return render(request,'trainedgerman.html',context_user )