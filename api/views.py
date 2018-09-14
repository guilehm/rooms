from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import RoomSerializer
from core.models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)
