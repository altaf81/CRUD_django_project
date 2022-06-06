from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm


def my_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req.POST)
        uname = req.POST['username']
        upass = req.POST['password']
        user = authenticate(req, username=uname, password=upass)
        if user:
            login(req, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(req, 'accountsapp/login.html', context)


def my_logout(req):
    logout(req)
    return redirect('home')


def register(req):
    if req.method == 'POST':
        form = MyUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MyUserCreationForm()
    context = {'form': form}
    return render(req, 'accountsapp/register.html', context)
