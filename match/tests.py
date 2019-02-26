from django.test import TestCase

from .models import User

# Create your tests here.
#import pytest

class LoginTests(TestCase):

    def test_login(self):
        e = User.objects.all()
        u = User(username="test1")
        self.assertIs(User.objects.filter(id="test1").exists(), True)