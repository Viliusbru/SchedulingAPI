from django.db import models
from django.contrib.auth.models import User

class MeetingRoom(models.Model):
    title = models.CharField(max_length=50)
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE)

