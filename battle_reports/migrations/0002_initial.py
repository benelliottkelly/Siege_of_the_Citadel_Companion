# Generated by Django 5.0.2 on 2024-02-21 23:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('battle_reports', '0001_initial'),
        ('corporations', '0001_initial'),
        ('experience', '0001_initial'),
        ('levels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='battlereport',
            name='corportations_playing',
            field=models.ManyToManyField(related_name='battles_participated', through='experience.Experience', to='corporations.corporation'),
        ),
        migrations.AddField(
            model_name='battlereport',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battle_reports', to='levels.level'),
        ),
        migrations.AddField(
            model_name='battlereport',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battle_reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='battlereport',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battles_won', to='corporations.corporation'),
        ),
    ]
