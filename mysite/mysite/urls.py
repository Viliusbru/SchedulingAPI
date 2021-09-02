from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapi.views import MeetingRoomList, MeetingRoomDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MeetingRoomList.as_view()),
    path('room/<int:pk>', MeetingRoomDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]