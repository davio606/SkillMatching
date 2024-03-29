# Generated by Django 2.1.7 on 2019-03-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20190320_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pic')),
                ('name', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='match.User'),
        ),
    ]
