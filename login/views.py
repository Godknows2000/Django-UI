from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from main.views import index_view

def login_view(request):
    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index_view)
        else:
            messages.success(request, "Invalid credentials, please try again!")
            return redirect("login")
    else:
        return render(request, 'login/login.html', {})
    
def logout_view(request):
    logout(request)
    return redirect(login_view)   

