from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tonnage = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CsvFile(models.Model):
    upload_time = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="uploads/")
