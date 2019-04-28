from django.test import TestCase
from django.test import Client
from .models import User, profile

from django.urls import resolve

# Create your tests here.
#import pytest

class IndexpageURLRedirectTests(TestCase):

    def test_homepage_url(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'match:index')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.view_name, 'login')

    def test_signup_url(self):
        resolver = resolve('/register/')
        self.assertEqual(resolver.view_name, 'register')

    def test_about_url(self):
        resolver = resolve('/match/about/')
        self.assertEqual(resolver.view_name, 'match:about')

    def test_suggest_url(self):
        resolver = resolve('/match/suggest/')
        self.assertEqual(resolver.view_name, 'match:suggest')

    def test_contact_url(self):
        resolver = resolve('/match/contact/')
        self.assertEqual(resolver.view_name, 'match:contact')
    
    def test_email_url(self):
        resolver = resolve('/match/email/')
        self.assertEqual(resolver.view_name, 'match:email')

    def test_calendar_url(self):
        resolver = resolve('/match/calendar/')
        self.assertEqual(resolver.view_name, 'match:calendar')

    def test_event_url(self):
        resolver = resolve('/match/event/')
        self.assertEqual(resolver.view_name, 'match:event')

class HomepageAfterLogin(TestCase):
    def test_to_homepage_after_login(self):
        resolver = resolve('/$/')
        self.assertEqual(resolver.view_name, 'match:home')

    def test_to_suggest_after_login(self):
        resolver = resolve('/suggest/')
        self.assertEqual(resolver.view_name, 'match:suggest')

    def test_to_calendar_after_login(self):
        resolver = resolve('/calendar/')
        self.assertEqual(resolver.view_name, 'match:calendar')

    def test_to_event_after_login(self):
        resolver = resolve('/event/')
        self.assertEqual(resolver.view_name, 'match:event')

    def test_contact_url(self):
        resolver = resolve('/contact/')
        self.assertEqual(resolver.view_name, 'match:contact')
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test", email="test@virginia.edu", password="test123")
    def test_username(self):
        a = User.objects.get_by_natural_key(username="test")
        self.assertEqual(a.username, "test")
    def test_major(self):
        a = User.objects.get_by_natural_key(username="test")
        a.profile.major = "Computer Science"
        self.assertEqual(a.profile.major, "Computer Science")
    def test_skills(self):
        a = User.objects.get_by_natural_key(username="test")
        a.profile.skills = "Java, C++"
        self.assertEqual(a.profile.skills, "Java, C++")
    def test_email(self):
        a = User.objects.get_by_natural_key(username="test")
        self.assertEqual(a.email, "test@virginia.edu")



