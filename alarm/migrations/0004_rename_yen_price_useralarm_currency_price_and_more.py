# Generated by Django 4.1.3 on 2022-12-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0003_rename_user_alarm_id_onoffrecord_user_alarm_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralarm',
            old_name='yen_price',
            new_name='currency_price',
        ),
        migrations.AddField(
            model_name='useralarm',
            name='which_currency',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
