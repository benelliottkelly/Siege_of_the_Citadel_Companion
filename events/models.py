from django.db import models

class Event(models.Model):
  number = models.PositiveIntegerField()
  title = models.CharField(max_length=255)
  text = models.TextField(max_length=2000)
  reinforcements = models.TextField(max_length=2000, default='Draw as many force cards as there are Corporation players')

  def __str__(self):
    return f'{self.number}: {self.title}'