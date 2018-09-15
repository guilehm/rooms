from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import MeetingSerializer, RoomSerializer
from core.models import Meeting, Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (AllowAny,)
