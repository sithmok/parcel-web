# Generated by Django 3.0 on 2022-05-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0059_auto_20220512_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profilePicture/profile-default-1.jpg', null=True, upload_to='profilePicture'),
        ),
    ]