# Generated by Django 3.0 on 2019-12-11 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191211_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='created',
            new_name='dateCreated',
        ),
        migrations.AddField(
            model_name='transaction',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
