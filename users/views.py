from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from.forms import SignupForm
from . import views
from .models import BlogUser


def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")  
    
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if (user is not None):
            login(request, user)
            return redirect("home")
        else:
            return render(request, "users/login.html")


def logout_view(request):
   logout(request)
   return redirect("home")


def signup_view(request):
    if request.method=="GET":
        form = SignupForm()
        return render(request, "users/signup.html", {"form":form})
    
    if request.method=="POST":
        form=SignupForm(request.POST, request.FILES)
        if form.is_valid():
            if user.profile_picture is None:
                pass
            else:
                user = form.save(
                    commit = False
                )
                user.username = f"{str.lower(user.first_name).split()[0]}{str.lower(user.last_name).split()[0]}"
                user.save()
                return redirect("login")
                
 
# Create your views here.
