from django.db import models

class Route(models.Model):
    delivery = models.CharField(max_length=10,
        choices=[("internal", "internal"), ("in", "in"), ("out", "out")], default="internal")
    start = models.CharField(max_length=100, null=True) # TODO: define format
    end = models.CharField(max_length=100, null=True) # TODO: define format
    product = models.CharField(max_length=100, null=True) # TODO: define choices
    quantity = models.PositiveIntegerField(default=0) # in tons
    duration_max = models.PositiveIntegerField(default=0) # in minutes

    # distances in meters, durations in minutes and energy in kWh
    distance_train = models.PositiveIntegerField(default=0)
    duration_train = models.PositiveIntegerField(default=0)
    energy_train = models.CharField(max_length=100, null=True) # TODO: define choices
    distance_truck = models.PositiveIntegerField(default=0)
    duration_truck = models.PositiveIntegerField(default=0)
    energy_truck = models.CharField(max_length=100, null=True) # TODO: define choices
    distance_ship = models.PositiveIntegerField(default=0)
    duration_ship = models.PositiveIntegerField(default=0)
    energy_ship = models.CharField(max_length=100, null=True) # TODO: define choices
    distance_plane = models.PositiveIntegerField(default=0)
    duration_plane = models.PositiveIntegerField(default=0)
    energy_plane = models.CharField(max_length=100, null=True) # TODO: define choices
    distance_bike = models.PositiveIntegerField(default=0)
    duration_bike = models.PositiveIntegerField(default=0)
    energy_bike = models.CharField(max_length=100, null=True) # TODO: define choices
    name_others = models.CharField(max_length=100, null=True)
    distance_others = models.PositiveIntegerField(default=0)
    duration_others = models.PositiveIntegerField(default=0)
    energy_others = models.CharField(max_length=100, null=True) # TODO: define choices

    energy_goods = models.PositiveIntegerField(default=0) # in kWh
    frequency = models.PositiveIntegerField(default=0) # rides per year

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return self.name
