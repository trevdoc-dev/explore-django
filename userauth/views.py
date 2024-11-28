from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("edit_profile")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST["email"]
        user.full_name = request.POST["full_name"]
        user.save()
        messages.success(request, "Profile updated successfully.")
    return render(request, "edit_profile.html", {"user": request.user})
