# Generated by Django 3.0 on 2019-12-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191211_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
