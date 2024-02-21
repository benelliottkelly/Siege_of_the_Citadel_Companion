from django.db import models

class Experience(models.Model):
  owner = models.ForeignKey(
    to='users.User',
    on_delete=models.CASCADE,
    related_name='experience'
  )
  battle_report = models.ForeignKey(
    to='battle_reports.BattleReport',
    on_delete=models.CASCADE,
    related_name='experience'
  )
  corporation = models.ForeignKey(
    to='corporations.Corporation',
    on_delete=models.CASCADE,
    related_name='experience'
  )
  corporation_level = models.PositiveIntegerField()
  exp_above_level = models.PositiveIntegerField(default=0)