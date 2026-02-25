from django.db import models
from rest_framework import fields

class Level(models.Model):
  # TILES = (
  #   (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16)
  # )
  def default_map():
    return {
        "width": 0,
        "height": 0,
        "tiles": [],
    }

  campaign = models.PositiveSmallIntegerField()
  mission = models.PositiveSmallIntegerField()
  name = models.CharField(max_length=255, null=True)
  map_tiles = models.JSONField(blank=True, default=default_map)
  dark_legion_entrance_points = models.ManyToManyField(
    to='entrance_points.EntrancePoint',
    related_name='levels'
  )
  additional_setup = models.TextField(max_length=2000, blank=True)
  time_limit = models.PositiveSmallIntegerField()
  potential_events = models.ManyToManyField(
    to='events.Event',
    related_name='levels'
  )
  dark_legion_resources = models.ManyToManyField(
    to='dark_legion.DarkLegion',
    related_name='levels'
  )

  def __str__(self):
    return f'Campaign {self.campaign} : Mission {self.mission} .'