from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapi.views import MeetingRoomList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MeetingRoomList.as_view()),
]