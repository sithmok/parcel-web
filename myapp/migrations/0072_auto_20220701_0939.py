# Generated by Django 3.0 on 2022-07-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0071_auto_20220701_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document1',
            field=models.FileField(blank=True, null=True, upload_to='document1/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='document2',
            field=models.FileField(blank=True, null=True, upload_to='document2/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='document3',
            field=models.FileField(blank=True, null=True, upload_to='document3/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='document4',
            field=models.FileField(blank=True, null=True, upload_to='document4/'),
        ),
    ]
