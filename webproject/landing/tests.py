import email
import os

from django.core.mail import send_mail
from django.test import TestCase

# Create your tests here.
import pytest

@pytest.mark.django_db
class TestEmail:
    def test_send_email(self, first_name=None, last_name=None, message=None):
        send_mail(message, message, 'you.aouali@gmail.com', ['you.aouali@gmail.com'])
