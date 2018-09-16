import logging

from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import MeetingSerializer, RoomSerializer
from core.models import Meeting, Room

logger = logging.getLogger('rooms')


class RoomFilterSet(FilterSet):
    class Meta:
        model = Room
        fields = [
            'slug',
            'active'
        ]


class MeetingFilterSet(FilterSet):
    class Meta:
        model = Meeting
        fields = [
            'room',
            'status'
        ]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)
    filter_class = RoomFilterSet


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (AllowAny,)
    filter_class = MeetingFilterSet
