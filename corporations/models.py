from django.db import models

class Corporation(models.Model):
  name = models.CharField(max_length=255)
  logo = models.CharField(max_length=500)
  corporation_special_ability_level_1 = models.TextField(max_length=3000)
  corporation_special_ability_level_2 = models.TextField(max_length=3000)
  corporation_special_ability_level_3 = models.TextField(max_length=3000)
  corporation_special_ability_level_4 = models.TextField(max_length=3000)
  corporation_special_ability_level_5 = models.TextField(max_length=3000)
  corporation_special_ability_level_6 = models.TextField(max_length=3000)
  corporation_special_ability_level_7 = models.TextField(max_length=3000)
  corporation_special_ability_level_8 = models.TextField(max_length=3000)
  corporation_special_ability_level_9 = models.TextField(max_length=3000)
  corporation_special_ability_level_10 = models.TextField(max_length=3000)
  corporation_special_ability_level_11 = models.TextField(max_length=3000)
  corporation_special_ability_level_12 = models.TextField(max_length=3000)

  def __str__(self):
    return f'{self.name}'