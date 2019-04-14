from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from .views import home


from . import views

app_name = 'users'
urlpatterns = [
    path('<int:user_id>/profile/', views.profile, name='profile'),
    #url(r"^account/", include("account.urls")),
    #url(r"^teams/", include("pinax.teams.urls", namespace="pinax_teams")),
] 