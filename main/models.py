from datetime import date
from django.db import models
import uuid

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=32, primary_key=True)
    road = models.CharField(max_length=64)
    datetime_captured = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Vehicle'

    def __str__(self):
        return f"Vehicle {self.creation_date}"