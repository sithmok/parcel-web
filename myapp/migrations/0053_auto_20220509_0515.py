# Generated by Django 3.0 on 2022-05-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0052_auto_20220509_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
