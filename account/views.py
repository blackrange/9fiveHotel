from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html',{'massage_username':'username taken..'})
            elif User.objects.filter(email=email).exists():
                return render(request,'signup.html',{'massage_email':'email taken..'})
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('signup.html')
        else:
            return render(request,'signup.html',{'massage_password':'password not matching..'})
    else:

        return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')