# Generated by Django 3.0 on 2022-05-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_auto_20220509_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
