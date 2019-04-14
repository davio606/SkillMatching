from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import profile
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import profile
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings


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

def email(request):
    subject = "Suggestion from " + request.POST['fname'] + ' ' + request.POST['lname']
    message = 'From: ' + request.POST['email'] + '\n \n' + "Message: " + request.POST['subject']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['studentskillmatching@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    messages.success(request, f'Your suggestion has been sent!')
    return render(request, 'match/suggest.html')

def contact(request):
    #return HttpResponse("This is the contact page")
    return render(request, 'match/contact.html')

def choose(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
        u_form.fields['username'].disabled = True
        u_form.fields['email'].disabled = True
        p_form.fields['image'].disabled = True
        p_form.fields['major'].disabled = True
        p_form.fields['skill'].disabled = True
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
    }
    return render(request, 'users/noEditProfile.html', context)

@login_required
def home(request):
    #users = User.objects.all()
    profiles = profile.objects.all()

    if 'search' in request.GET:
        search_term = request.GET['search']
        #users = users.filter(username__icontains=search_term)
        profiles = profiles.filter(Q(user__username__icontains=search_term) | Q(major__icontains=search_term) | Q(skill__icontains=search_term))

    context = {
        #'user_list': users,
        'profile_list': profiles,
    }
    return render(request, 'match/home.html', context)