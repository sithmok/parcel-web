# Generated by Django 3.0 on 2022-06-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0062_auto_20220603_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='document2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='document3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='document4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]