from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    user = request.user

    if user.is_authenticated:
        return HttpResponse(f"This is the home page, current user: {user.username}")
    else: 
        return HttpResponse("User is not logged in")
    #return render(request, 'index.html')
