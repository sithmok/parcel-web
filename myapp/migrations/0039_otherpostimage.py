# Generated by Django 3.0 on 2022-03-29 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_post_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='otherPostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='otherPostImage/')),
                ('image_name', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Post')),
            ],
        ),
    ]
