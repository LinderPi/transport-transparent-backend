from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tonnage = models.PositiveIntegerField(default=0)
    distance_train = models.PositiveIntegerField(default=0)
    distance_truck = models.PositiveIntegerField(default=0)
    distance_ship = models.PositiveIntegerField(default=0)
    distance_plane = models.PositiveIntegerField(default=0)
    distance_bike = models.PositiveIntegerField(default=0)
    distance_others = models.PositiveIntegerField(default=0)
    transports_per_day = models.PositiveIntegerField(default=0)
    short_term = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CsvFile(models.Model):
    upload_time = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="uploads/")
