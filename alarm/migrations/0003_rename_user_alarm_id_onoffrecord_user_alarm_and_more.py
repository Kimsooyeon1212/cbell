# Generated by Django 4.1.3 on 2022-12-01 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_useralarm_onoffrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onoffrecord',
            old_name='user_alarm_id',
            new_name='user_alarm',
        ),
        migrations.RenameField(
            model_name='useralarm',
            old_name='user_id',
            new_name='user',
        ),
    ]
