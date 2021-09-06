from .models import MeetingRoom, RoomReservation
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import ValidationError
from .serializers import MeetingRoomSerializer, UserSerializer, ReservationSerializer, RoomReservationSerializer


class MeetingRoomList(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

class Reservation(generics.ListCreateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoomReservation(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(organizer=self.request.user)

    # def get_queryset(self):
    #     user = self.kwargs['organizer']
    #     return Reservation.objects.filter(organizer__username=user)