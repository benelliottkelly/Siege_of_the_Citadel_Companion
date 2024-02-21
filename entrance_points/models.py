from django.db import models
from rest_framework import fields

class EntrancePoint(models.Model):
  DIRECTIONS = (
    ('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West'))
  map_tile = models.PositiveIntegerField()
  cardinal_direction = models.CharField(choices=DIRECTIONS)

  def __str__(self):
    return f'{self.map_tile}: {self.cardinal_direction}'