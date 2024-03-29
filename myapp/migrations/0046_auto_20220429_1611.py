# Generated by Django 3.0 on 2022-04-29 09:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_auto_20220419_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='money_type',
            field=models.CharField(choices=[('วัน', 'วัน'), ('สัปดาห์', 'สัปดาห์'), ('เดือน', 'เดือน')], default='วัน', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile')),
            ],
        ),
    ]
