# Generated by Django 3.0.5 on 2020-05-04 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenApp', '0003_auto_20200504_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esp41',
            old_name='temperature',
            new_name='temperatureEsp',
        ),
    ]
