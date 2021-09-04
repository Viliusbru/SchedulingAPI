from django.db import models
from django.contrib.auth.models import User

class MeetingRoom(models.Model):
    room_number = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, 
        default=User, 
        null=True, 
        on_delete=models.CASCADE)
    created = models.DateTimeField(
        auto_now_add=True, 
        null=True)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return self.room_number


class RoomReservation(models.Model):
    STATUS_VALID = 0
    STATUS_CANCELLED = 1
    STATUS_TYPES = [
        (STATUS_VALID, "Valid"),
        (STATUS_CANCELLED, "Reserved"),
    ]
    room = models.ForeignKey(
        MeetingRoom,
        related_name="reservations",
        on_delete=models.CASCADE
    )
    organizer = models.ForeignKey(
        User,
        related_name="organized_reservations",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    status = models.IntegerField(
        choices=STATUS_TYPES,
        default=STATUS_VALID
    )
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self):
        return self.title