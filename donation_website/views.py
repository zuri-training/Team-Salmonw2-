from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

# Create your views here.
@login_required(login_url="/users/login")
def main(request):
    return render(request, "donate_website/main.html")


def index(request):
    user = request.user

    """
    if user.is_authenticated:
        return HttpResponse(f"This is the home page, current user: {user.username}")
    else: 
        return HttpResponse("User is not logged in")
    """

    return render(request, 'donate_website/index.html')


def donate(request):
    return render(request, 'donate_website/donate.html')

def checkout_page(request):
    return render(request, 'donate_website/checkout.html')

class MakeDonationView(CreateView):
    model = Donate
    fields = "__all__"
    template_name = "donate_website/donate.html"
    success_url = reverse_lazy("checkout")


def contact_us(request):
    return render(request, 'donate_website/contact.html')

def about_us(request):
    return render(request, 'donate_website/about.html')