# Generated by Django 5.0.2 on 2024-02-21 23:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('corporations', '0001_initial'),
        ('levels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_players', models.PositiveSmallIntegerField()),
                ('use_computer_to_draw_reinforcements', models.BooleanField(default=True)),
                ('corporations', models.ManyToManyField(related_name='game_setups', to='corporations.corporation')),
                ('mission', models.ManyToManyField(related_name='game_setups', to='levels.level')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_setups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
