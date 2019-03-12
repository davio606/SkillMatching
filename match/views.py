from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django import template

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

def suggest(request):
    #return HttpResponse("This is the suggest page")
    return render(request, 'match/suggest.html')

def contact(request):
    #return HttpResponse("This is the contact page")
    return render(request, 'match/contact.html')

def home(request):
    return render(request, 'match/home.html')

def profile(request):
    return render(request, 'match/profile.html')

def submit(request):
    model = User
    usernm = request.POST['username']
    passwd = request.POST['password']
    user_list = User.objects.all()
    

    if (User.objects.filter(username=usernm, password=passwd).exists()):
        context = {'user_list': user_list, 'invalid': False}
        return render(request, 'match/home.html', context)
    else: 
        return render_to_response("match/login2.html", {'invalid': True })