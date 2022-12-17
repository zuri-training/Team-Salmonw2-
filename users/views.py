from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, DeleteView
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib import messages
# Create your views here.
def user_login(request):
    form = LoginForm(request.POST or None)

    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                messages.error(request, "Invalid Credentials, Try Again")
        else:
            messages.error(request, "Error Valid Details, Try Again")

    return render(request, "users/login.html", {"form": form, "msg": msg})


def user_register(request):

    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            messages.success(request, "User Created Successfully")
            success = True

            return redirect("login")

        else:
            messages.error(request, "Incorrect Password or Username")
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form, "msg": msg, "success": success})
