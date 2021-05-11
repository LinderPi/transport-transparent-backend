from django.db import models

class Route(models.Model):
    start = models.CharField(max_length=100, null=True) # TODO: define format
    end = models.CharField(max_length=100, null=True) # TODO: define format
    distance = models.PositiveIntegerField(default=0) # in kilometers
    duration = models.PositiveIntegerField(default=0) # in minutes
    quantity = models.PositiveIntegerField(default=0) # in tons
    transportation = models.CharField(max_length=10,
        choices=[("train", "train"), ("truck", "truck"), ("ship", "ship"), ("plane", "plane"), ("others", "others")],
        default="others")
    delivery = models.CharField(max_length=10,
        choices=[("internal", "internal"), ("in", "in"), ("out", "out")], default="internal")
    energy_goods = models.PositiveIntegerField(default=0) # in kWh
    frequency = models.PositiveIntegerField(default=0) # rides per year

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return self.name
