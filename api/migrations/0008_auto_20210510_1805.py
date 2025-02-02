# Generated by Django 3.2 on 2021-05-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210510_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='delivery',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='duration_max',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='emissions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='end',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_bike',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_others',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_plane',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_ship',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_train',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='energy_truck',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='name_others',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='product',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='start',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
