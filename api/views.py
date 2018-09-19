import logging

from django_filters import FilterSet, TimeFilter
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
        ]


class MeetingFilterSet(FilterSet):
    start_gte = TimeFilter(field_name='start', lookup_expr='gte')
    end_lte = TimeFilter(field_name='end', lookup_expr='lte')

    class Meta:
        model = Meeting
        fields = [
            'room',
            'status',
            'date',
            'start',
            'end',
            'start_gte',
            'end_lte',
        ]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)
    filterset_class = RoomFilterSet


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (AllowAny,)
    filterset_class = MeetingFilterSet
