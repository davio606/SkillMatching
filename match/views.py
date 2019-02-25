from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import User

def index(request):
    return HttpResponse("This is our student matching app")

def login(request):
    #return HttpResponse("This is the login page")
    return render(request, 'match/login.html')

def submit(request):
    usernm = request.POST['username']
    passwd = request.POST['password']

    if (User.objects.filter(username=usernm, password=passwd).exists()):
        return HttpResponse("You are logged in")
    else: 
        return HttpResponse("Username or Password Incorrect")