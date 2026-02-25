from django.db import models

class DarkLegion(models.Model):
  card_number = models.PositiveIntegerField()
  name = models.CharField(max_length=255)
  image = models.CharField(max_length=550)
  subheading = models.CharField(max_length=550, blank=True)
  description = models.TextField(max_length=2000, blank=True)
  draw_one_more = models.BooleanField(blank=False, default=False)
  stop_drawing = models.BooleanField(blank=False, default=False)
  remove_after_drawing = models.BooleanField(blank=False, default=False)
  choice = models.JSONField(blank=True, default=list)

  def __str__(self):
    return f'{self.card_number}: {self.name}'
