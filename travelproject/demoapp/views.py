from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import place
from .models import people
# Create your views here.
from django.http import HttpResponse


def demo(request):
    obj = place.objects.all()
    obj1 = people.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid User Name")
            return redirect("login")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User id Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
            user.save()
            print("User created")
            return redirect("login")
        else:
            messages.info(request, "Password Not Matched")
            print("Password error")
            return redirect('register')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
