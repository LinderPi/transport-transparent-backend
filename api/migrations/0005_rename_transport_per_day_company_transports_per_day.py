# Generated by Django 3.2 on 2021-05-10 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210510_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='transport_per_day',
            new_name='transports_per_day',
        ),
    ]
