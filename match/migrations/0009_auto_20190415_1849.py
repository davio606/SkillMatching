# Generated by Django 2.1.5 on 2019-04-15 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
