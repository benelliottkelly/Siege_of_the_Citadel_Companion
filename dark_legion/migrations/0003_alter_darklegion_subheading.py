# Generated by Django 5.0.2 on 2024-03-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dark_legion', '0002_darklegion_subheading_alter_darklegion_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darklegion',
            name='subheading',
            field=models.CharField(blank=True, max_length=550),
        ),
    ]
