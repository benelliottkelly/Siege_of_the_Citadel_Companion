# Generated by Django 5.0.2 on 2024-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BattleReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number_of_players', models.PositiveSmallIntegerField()),
                ('notes', models.TextField(blank=True, max_length=3000, null=True)),
            ],
        ),
    ]
