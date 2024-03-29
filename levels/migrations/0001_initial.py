# Generated by Django 5.0.2 on 2024-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dark_legion', '0001_initial'),
        ('entrance_points', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.PositiveSmallIntegerField()),
                ('mission', models.PositiveSmallIntegerField()),
                ('additional_setup', models.TextField(max_length=2000)),
                ('time_limit', models.PositiveSmallIntegerField()),
                ('dark_legion_entrance_points', models.ManyToManyField(related_name='levels', to='entrance_points.entrancepoint')),
                ('dark_legion_resources', models.ManyToManyField(related_name='levels', to='dark_legion.darklegion')),
                ('potential_events', models.ManyToManyField(related_name='levels', to='events.event')),
            ],
        ),
    ]
