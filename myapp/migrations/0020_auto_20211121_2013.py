# Generated by Django 3.0 on 2021-11-21 13:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0019_auto_20211121_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='Intern_type',
            field=models.CharField(choices=[('ฝึกงาน', 'ฝึกงาน'), ('งานประจำ', 'งานประจำ'), ('ฟรีแลนซ์', 'ฟรีแลนซ์'), ('พาร์ทไทม์', 'พาร์ทไทม์'), ('สัญญาจ้าง', 'สัญญาจ้าง')], default='ฝึกงาน', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.CharField(default='ไม่มี', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Province'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('น้อยมาก', 'น้อยมาก'), ('น้อย', 'น้อย'), ('พอใช้', 'พอใช้'), ('มาก', 'มาก'), ('มากที่สุด', 'มากที่สุด')], default='พอใช้', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, default='Hi! Im new user', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='prov_name',
            field=models.CharField(default='1', max_length=255),
        ),
    ]