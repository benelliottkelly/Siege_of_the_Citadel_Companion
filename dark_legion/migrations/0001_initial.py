# Generated by Django 5.0.2 on 2024-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DarkLegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=550)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
    ]
