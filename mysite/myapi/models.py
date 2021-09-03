from django.db import models
from django.contrib.auth.models import User

class MeetingRoom(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, default=User, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created']
# class RoomReservation(models.Model):
#     title = models.ForeignKey(MeetingRoom, null=True, on_delete=models.CASCADE)