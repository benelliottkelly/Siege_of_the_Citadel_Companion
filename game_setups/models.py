from django.db import models

class GameSetup(models.Model):
  owner = models.ForeignKey(
    to='users.User',
    on_delete=models.CASCADE,
    related_name='game_setups'
  )
  mission = models.ManyToManyField(
    to='levels.Level',
    related_name='game_setups'
  )
  number_of_players = models.PositiveSmallIntegerField()
  corporations = models.ManyToManyField(
    to='corporations.Corporation',
    related_name='game_setups'
  )
  use_computer_to_draw_reinforcements = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.owner}s mission on mission {self.mission}'