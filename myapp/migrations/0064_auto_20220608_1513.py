# Generated by Django 3.0 on 2022-06-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0063_auto_20220608_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apply',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='Intern_type',
            field=models.CharField(choices=[('ปกติ', 'ปกติ'), ('สหกิจ', 'สหกิจ')], max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='usertype',
            field=models.CharField(choices=[('member', 'member'), ('student', 'student'), ('admin', 'admin')], default='member', max_length=100),
        ),
        migrations.CreateModel(
            name='StudentPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificationNumber', models.IntegerField()),
                ('approve', models.BooleanField(default=False)),
                ('applyDate', models.DateTimeField(auto_now_add=True)),
                ('approveDate', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile')),
            ],
        ),
    ]
