# Generated by Django 3.0 on 2021-11-30 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
