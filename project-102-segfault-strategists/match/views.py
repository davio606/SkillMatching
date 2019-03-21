from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import User


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

@login_required
def home(request):
    users = User.objects.all()

    if 'search' in request.GET:
        search_term = request.GET['search']
        users = users.filter(username__icontains=search_term)

    context = {'user_list': users}
    return render(request, 'match/home.html', context)

@login_required
def profile (request):
    return render (request, 'match/profile.html')
