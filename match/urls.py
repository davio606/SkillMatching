from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views
from .views import home


from . import views

app_name = 'match'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login2'),
    path('auth/', include('social_django.urls'), name='social'), 
    path('$/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('about/', views.about, name='about'),
    path('suggest/', views.suggest, name='suggest'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
]