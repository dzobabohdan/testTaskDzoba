from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=50, min_length=3)
    species = models.CharField(max_length=50)
    watering_frequency_days = models.FloatField()
    last_watered_date = models.DateField()

    def __str__(self):
        return self.name
