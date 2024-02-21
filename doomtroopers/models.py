from django.db import models

class Doomtrooper(models.Model):
  name = models.CharField(max_length=255)
  picture = models.CharField(max_length=500)
  corporation = models.ForeignKey(
    to='corporations.Corporation',
    on_delete=models.CASCADE,
    related_name='doomtroopers'
  )
  specialist_type = models.ForeignKey(
    to='specialist_types.SpecialistType',
    on_delete=models.CASCADE,
    related_name='doomtroopers'
  )
  description = models.TextField(max_length=2000)

  def __str__(self):
    return f'{self.name}'