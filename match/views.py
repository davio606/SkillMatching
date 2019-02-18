from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("This is our student matching app")

def login(request):
    #return HttpResponse("This is the login page")
    return render(request, 'match/login.html')

def submit(request):
    return HttpResponse("You are logged in")