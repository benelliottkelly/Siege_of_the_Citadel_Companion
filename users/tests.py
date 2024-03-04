import json
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

# As the DB is hosted on a free tier server, seperate test_DBs cannot be created due to permission issues
# Therefore to run tests we need to use the existing DB using <python manage.py test --keepdb>
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

class UserViewSetTestCase(APITestCase):

  def setUp(self):
    # Because we are keeping the DB rather than creating a new test_DB we need to specify the pk, as there is already existing users and the PK will go up each time a test is run
    self.user = User.objects.create_user(pk=999, username='testuser3', email='testuser3@email.com', password='another_unique_password')
    self.token = RefreshToken.for_user(self.user)
    self.api_authentication()

  def api_authentication(self):
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

  # Test the endpoint for a single profile page while logged in
  def test_user_detail_retrieve(self):
    # Test the response for testuser3 looking at their own profile
    response = self.client.get(reverse('user-detail', kwargs={'pk': 999}))
    # Test the return of a 200 status code
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    # Test the username retrieved is the one expected
    self.assertEqual(response.data['username'], 'testuser3')
  
  # Test for user to update their own profile
  def test_user_updated_by_owner(self):
    response = self.client.patch(reverse('user-detail', kwargs={'pk': 999}), {'first_name': 'Testy', 'last_name': 'McTestFace'})    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {'pk': 999, 'first_name': 'Testy', 'last_name': 'McTestFace', 'username': 'testuser3', 'email': 'testuser3@email.com', 'image': ''})

  # Test for user trying to update someone else's profile
  def test_user_updated_by_random_user(self):
    random_user = User.objects.create_user(username='random', password='more_unique_passwords')
    self.client.force_authenticate(user=random_user)
    response = self.client.patch(reverse('user-detail', kwargs={'pk': 999}), {'first_name': 'Rude', 'last_name': 'Names'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)