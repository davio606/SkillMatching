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


from .models import Message
from datetime import timedelta
import datetime
import dateutil.parser
from pytz import timezone
import pytz
from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
service_account_email = 'segfaultstrategists@studentskillmatching.iam.gserviceaccount.com'
CLIENT_SECRET_FILE = 'studentskillmatching.json'


def index(request):
    #return HttpResponse("This is our student matching app")
    return render(request, 'match/index.html')


def suggest(request):
    #return HttpResponse("This is the suggest page")
    return render(request, 'match/suggest.html')



def message(request):
    # return HttpResponse("This is the message page")
    profiles = profile.objects.all()
    messages = Message.objects.all()

    context = {
        'profile_list': profiles,
        'message_list': messages,
    }

    return render(request, 'match/message.html', context)

def send(request):
    m = Message(sender=request.POST['userFrom'], receiver=request.POST['userTo'],message_content=request.POST['content'], subject=request.POST['subject'])
    m.save()
    return render(request, 'match/success.html')

def calendar(request):
    #return HttpResponse("This is the calendar page")
    return render(request, 'match/calendar.html')

def event(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = ServiceAccountCredentials.from_json_keyfile_name(filename=CLIENT_SECRET_FILE, scopes=SCOPES)
    http = creds.authorize(httplib2.Http())
    service = build('calendar', 'v3', http=http)

    Summary = request.POST['ename']
    Description = request.POST['edesc']
    if(request.POST['sdate']):
        Date = request.POST['sdate']
        parseDate = timezone('US/Eastern').localize(dateutil.parser.parse(Date))
        parseDate_plusone = parseDate + timedelta(hours=1)
    else:
        Date = datetime.datetime.now(tz=pytz.utc).isoformat()
        parseDate = dateutil.parser.parse(Date)
        parseDate_plusone = parseDate + timedelta(hours=1)

    event = service.events().insert(calendarId='studentskillmatching@gmail.com', body={
        'summary': Summary,
        'description': Description,
        'start': {'dateTime': parseDate.isoformat()},
        'end': {'dateTime': (parseDate_plusone).isoformat()},
    }).execute()

    return render(request, 'match/calendar.html')
    #return HttpResponse(parseDate_plusone)

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