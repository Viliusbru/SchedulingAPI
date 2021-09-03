from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField
from .models import MeetingRoom
from django.contrib.auth.models import User


class MeetingRoomSerializer(serializers.ModelSerializer):
    detail_view = serializers.HyperlinkedIdentityField(view_name='room_detail', format='html')
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    # created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", input_formats=None)
    class Meta:
        model = MeetingRoom
        fields = ['id', 'title', 'user', 'user_id', 'detail_view', 'created']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

