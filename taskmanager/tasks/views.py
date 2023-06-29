from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Film




def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, 'auth.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Аккаунта " + str(username) + " не существует")
    return render(request, "auth.html")

def log_out(request):
    logout(request)
    return redirect('login')


def homepage(request):
    if request.user.is_authenticated:
        username = request.user.username
        films = Film.objects.all()
        return render(request, 'home.html', {
            'username': username,
            'films': films
            })
    else:
        return redirect('login')


def register(request):
    if request.method == "GET":
        form = CreateUserForm()
        data = {"form": form}
        return render(request, 'register.html', context=data)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')
        else:
            
            messages.error(request, "Ошибка, проверьте данные")
    return render(request, 'register.html', {})