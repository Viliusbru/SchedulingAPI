from rest_framework import serializers
from .models import MeetingRoom

class MeetingRoomSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = MeetingRoom
        fields = ['id', 'title', 'user']
