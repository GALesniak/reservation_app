from datetime import date

from django.db import models
from django.utils.timezone import now
today = date.today()







class Room(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    room_name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField(4, 0, null=True, blank=True)
    projector = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False)
    date_now = models.DateTimeField(blank=False, default=now)


class Booking(models.Model):
    booking_in = models.DateTimeField()
    booking_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)






