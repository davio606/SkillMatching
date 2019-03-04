from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response

from .models import User

def index(request):
    #return HttpResponse("This is our student matching app")
    return render(request, 'match/index.html')

def login(request):
    #return HttpResponse("This is the login page")
    return render(request, 'match/login2.html')

def signup(request):
    #return HttpResponse("This is the signup page")
    return render(request, 'match/login2.html')

def about(request):
    #return HttpResponse("This is the about page")
    return render(request, 'match/about.html')

def submit(request):
    usernm = request.POST['username']
    passwd = request.POST['password']

    if (User.objects.filter(username=usernm, password=passwd).exists()):
        return HttpResponse("You are logged in")
    else: 
        return render_to_response("match/login2.html", 
                       {'invalid': True })