# Generated by Django 5.0.2 on 2024-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=2000)),
                ('reinforcements', models.TextField(default='Draw as many force cards as there are Corporation players', max_length=2000)),
            ],
        ),
    ]