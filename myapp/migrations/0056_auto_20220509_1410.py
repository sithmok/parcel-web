# Generated by Django 3.0 on 2022-05-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0055_auto_20220509_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
