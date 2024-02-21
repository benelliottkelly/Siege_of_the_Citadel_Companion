from django.db import models

class SpecialistType(models.Model):
  name = models.CharField(max_length=255)
  picture = models.CharField(max_length=550)

  def __str__(self):
    return f'{self.name}'