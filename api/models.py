from django.db import models

class Route(models.Model):
    start = models.CharField(max_length=100) # TODO: define format
    end = models.CharField(max_length=100) # TODO: define format
    product = models.CharField(max_length=100) # TODO: define choices
    quantity = models.PositiveIntegerField() # in tons
    duration_max = models.PositiveIntegerField() # in minutes

    # distances in meters, durations in minutes and energy in kWh
    distance_train = models.PositiveIntegerField(default=0)
    duration_train = models.PositiveIntegerField(default=0)
    energy_train = models.PositiveIntegerField(default=0)
    distance_truck = models.PositiveIntegerField(default=0)
    duration_truck = models.PositiveIntegerField(default=0)
    energy_truck = models.PositiveIntegerField(default=0)
    distance_ship = models.PositiveIntegerField(default=0)
    duration_ship = models.PositiveIntegerField(default=0)
    energy_ship = models.PositiveIntegerField(default=0)
    distance_plane = models.PositiveIntegerField(default=0)
    duration_plane = models.PositiveIntegerField(default=0)
    energy_plane = models.PositiveIntegerField(default=0)
    distance_bike = models.PositiveIntegerField(default=0)
    duration_bike = models.PositiveIntegerField(default=0)
    energy_bike = models.PositiveIntegerField(default=0)
    name_others = models.PositiveIntegerField(null=True)
    distance_others = models.PositiveIntegerField(default=0)
    duration_others = models.PositiveIntegerField(default=0)
    energy_others = models.PositiveIntegerField(default=0)

    energy_goods = models.PositiveIntegerField(default=0) # in kWh
    emissions = models.PositiveIntegerField() # TODO: probably to be calculated

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return self.name
