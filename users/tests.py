import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from users.serializers.common import RegistrationSerializer, UserSerializer

class RegistrationTestCase(APITestCase):

  def test_registration(self):
    data = {'username': 'testuser', 'email': 'test@email.com', 'password': 'super_unique_password', 'password_confirmation': 'super_unique_password'}
    # Add a test user to database
    response = self.client.post('/api/auth/register/', data)
    # Test that 201 status is receieved
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
  def test_passwords_dont_match(self):
    data = {'username': 'testuser2', 'email': 'test2@email.com', 'password': 'super_unique_password', 'password_confirmation': 'different_unique_password'}
    # Add a second test user to database
    response = self.client.post('/api/auth/register/', data)
    # Test that 400 status is receieved
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)