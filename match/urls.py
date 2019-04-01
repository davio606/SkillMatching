from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from .views import home


from . import views

app_name = 'match'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
   #path('login/', views.login, name='login2'),
    path('auth/', include('social_django.urls'), name='social'), 
    path('$/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('suggest/', views.suggest, name='suggest'),
    path('contact/', views.contact, name='contact'),
    path('<int:user_id>/profile/', views.choose, name='choose')
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


