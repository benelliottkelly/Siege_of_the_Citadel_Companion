from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser has fields id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active and date_joined

class User(AbstractUser):
  email = models.EmailField(unique=True)
  image = models.CharField(max_length=500, blank=True)

  def __str__(self):
    return f'{self.username} {self.email}'