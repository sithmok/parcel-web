# Generated by Django 3.0 on 2021-11-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20211127_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='myapp.Profile'),
        ),
    ]