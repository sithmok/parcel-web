# Generated by Django 3.0 on 2021-11-21 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20211121_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Province'),
        ),
    ]