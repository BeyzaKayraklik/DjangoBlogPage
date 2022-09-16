from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_req(request):
    if request.user.is_authenticated:
        return redirect("blogs")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("blogs")
        else:
            return render(request, "account/login.html", {
                "error": "username or password is invalid"
            })
    return render(request, "account/login.html")


def register_req(request):
    if request.user.is_authenticated:
        return redirect("blogs")
    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error": "username is used",
                    "username": username,
                    "email": email,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {
                        "error": "mail is used",
                        "username": username,
                        "email": email,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", {
                "error": "passwords do not match",
                "username": username,
                "email": email,
            })

    return render(request, "account/register.html")


def logout_req(request):
    logout(request)
    return redirect("blogs")
