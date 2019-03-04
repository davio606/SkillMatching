from django.urls import path


from . import views

app_name = 'match'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login2'),
    path('submit/', views.submit, name='submit'),
    path('about/', views.about, name='about'),
    path('suggest/', views.suggest, name='suggest'),
    path('contact/', views.contact, name='contact'),

]