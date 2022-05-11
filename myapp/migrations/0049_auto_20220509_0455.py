# Generated by Django 3.0 on 2022-05-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_post_introduce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='money_type',
            field=models.CharField(blank=True, choices=[('วัน', 'วัน'), ('สัปดาห์', 'สัปดาห์'), ('เดือน', 'เดือน')], max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='internWorks',
        ),
    ]
