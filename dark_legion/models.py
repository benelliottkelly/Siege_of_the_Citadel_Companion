from django.db import models

class DarkLegion(models.Model):
  card_number = models.PositiveIntegerField()
  name = models.CharField(max_length=255)
  image = models.CharField(max_length=550)
  description = models.TextField(max_length=2000)

  def __str__(self):
    return f'{self.card_number}: {self.name}'
