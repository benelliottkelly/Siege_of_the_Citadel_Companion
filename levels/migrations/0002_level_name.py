# Generated by Django 5.0.2 on 2024-02-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
