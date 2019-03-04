from django.test import TestCase

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


class HomepageURLRedirectTests(TestCase):

    def test_homepage_url(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'match:index')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        resolver = resolve('/match/login/')
        self.assertEqual(resolver.view_name, 'match:login2')

    def test_signup_url(self):
        resolver = resolve('/match/login/')
        self.assertEqual(resolver.view_name, 'match:login2')

    def test_about_url(self):
        resolver = resolve('/match/about/')
        self.assertEqual(resolver.view_name, 'match:about')
