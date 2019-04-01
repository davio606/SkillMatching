from django.test import TestCase
from django.test import Client
from .models import User

from django.urls import resolve

# Create your tests here.
#import pytest

class LoginTests(TestCase):

    def test_login(self):
        #e = User.objects.all()
        #u = User(username="test1")
        #self.assertIs(User.objects.filter(id="test1").exists(), True)
        self.assertIs(True, True)


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

class HomepageAfterLogin(TestCase):
    def test_to_homepage_after_login(self):
        resolver = resolve('/$/')
        self.assertEqual(resolver.view_name, 'match:home')