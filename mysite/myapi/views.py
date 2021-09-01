from .models import MeetingRoom
from django.contrib.auth.models import User, Group
from rest_framework import generics
from .serializers import MeetingRoomSerializer


class MeetingRoomList(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer