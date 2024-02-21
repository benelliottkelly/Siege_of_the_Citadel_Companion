from django.db import models

class BattleReport(models.Model):
  owner = models.ForeignKey(
    to='users.User',
    on_delete=models.CASCADE,
    related_name='battle_reports'
  )
  level = models.ForeignKey(
    to='levels.Level',
    on_delete=models.CASCADE,
    related_name='battle_reports'
  )
  created_at = models.DateTimeField(auto_now_add=True)
  number_of_players = models.PositiveSmallIntegerField()
  corportations_playing = models.ManyToManyField(
    to='corporations.Corporation',
    through='experience.Experience',
    related_name='battles_participated'
  )
  winner = models.ForeignKey(
    to='corporations.Corporation',
    on_delete=models.CASCADE,
    related_name='battles_won'
  )
  notes = models.TextField(max_length=3000, blank=True, null=True)

  def __str__(self):
    return f'Battle ID: {self.pk}.'