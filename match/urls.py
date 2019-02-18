from django.urls import path

from . import views

app_name = 'match'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('submit/', views.submit, name='submit'),
]