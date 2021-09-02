from .models import MeetingRoom
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .serializers import MeetingRoomSerializer


class MeetingRoomList(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

class MeetingRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = MeetingRoom.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("You can't delete other people's inputs")

    def put(self, request, *args, **kwargs):
        post = MeetingRoom.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("You can't update other people's inputs")