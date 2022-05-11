# Generated by Django 3.0 on 2021-11-15 14:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_post_cate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.AddField(
            model_name='post',
            name='Intern_type',
            field=models.CharField(choices=[('ปกติ', 'ปกติ'), ('สหกิจ', 'สหกิจ')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, default='ไม่มี', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, default='ไม่มี', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, default='ไม่มี', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('น้อยมาก', 'น้อยมาก'), ('น้อย', 'น้อย'), ('พอใช้', 'พอใช้'), ('มาก', 'มาก'), ('มากที่สุด', 'มากที่สุด')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profile-default.png', null=True, upload_to='profilePicture'),
        ),
    ]