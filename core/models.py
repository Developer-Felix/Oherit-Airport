
from django.db import models
import phonenumbers

class Subscription(models.Model):
    mail = models.CharField(max_length=255)

    def __str__(self):
        return self.mail

class Booking(models.Model):
    curent_location = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    date_dep = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    no_of_persons = models.CharField(max_length=255)
    type_of_aircraft = models.CharField(max_length=255)
    name   = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} wants to travel from {self.curent_location} to {self.to} on {self.date_dep} at {self.time}'
    