# Generated by Django 3.0 on 2022-06-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0064_auto_20220608_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpending',
            name='studentCard',
            field=models.ImageField(null=True, upload_to='studentCard/'),
        ),
    ]