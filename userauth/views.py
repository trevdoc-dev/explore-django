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

        if user is not None:
            login(request, user)
            return redirect("edit_profile")  # Redirect to edit page after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required
def edit_profile(request):
    user = request.user  # Get the currently logged-in user

    if request.method == "POST":
        # Update user details
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.save()
        return render(request, "edit_profile.html", {"success": True})

    return render(request, "edit_profile.html", {"user": user})


def main_page(request):
    return render(request, "main_page.html")
