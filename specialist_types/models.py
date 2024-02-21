from django.db import models

class SpecialistType(models.Model):
  name = models.CharField(max_length=255)
  picture = models.CharField(max_length=550)
