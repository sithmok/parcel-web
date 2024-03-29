# Generated by Django 3.0 on 2021-11-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211115_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prov_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tel',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='post',
            name='prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Province'),
        ),
    ]
