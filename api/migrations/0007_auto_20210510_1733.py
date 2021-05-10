# Generated by Django 3.2 on 2021-05-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_delete_csvfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('duration_max', models.PositiveIntegerField()),
                ('distance_train', models.PositiveIntegerField(default=0)),
                ('duration_train', models.PositiveIntegerField(default=0)),
                ('energy_train', models.PositiveIntegerField(default=0)),
                ('distance_truck', models.PositiveIntegerField(default=0)),
                ('duration_truck', models.PositiveIntegerField(default=0)),
                ('energy_truck', models.PositiveIntegerField(default=0)),
                ('distance_ship', models.PositiveIntegerField(default=0)),
                ('duration_ship', models.PositiveIntegerField(default=0)),
                ('energy_ship', models.PositiveIntegerField(default=0)),
                ('distance_plane', models.PositiveIntegerField(default=0)),
                ('duration_plane', models.PositiveIntegerField(default=0)),
                ('energy_plane', models.PositiveIntegerField(default=0)),
                ('distance_bike', models.PositiveIntegerField(default=0)),
                ('duration_bike', models.PositiveIntegerField(default=0)),
                ('energy_bike', models.PositiveIntegerField(default=0)),
                ('name_others', models.PositiveIntegerField(null=True)),
                ('distance_others', models.PositiveIntegerField(default=0)),
                ('duration_others', models.PositiveIntegerField(default=0)),
                ('energy_others', models.PositiveIntegerField(default=0)),
                ('energy_goods', models.PositiveIntegerField(default=0)),
                ('emissions', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_bike',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_others',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_plane',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_ship',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_train',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distance_truck',
        ),
        migrations.RemoveField(
            model_name='company',
            name='short_term',
        ),
        migrations.RemoveField(
            model_name='company',
            name='tonnage',
        ),
        migrations.RemoveField(
            model_name='company',
            name='transports_per_day',
        ),
        migrations.AddField(
            model_name='company',
            name='routes',
            field=models.ManyToManyField(to='api.Route'),
        ),
    ]
