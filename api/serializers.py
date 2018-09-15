from rest_framework.serializers import ModelSerializer

from core.models import Meeting, Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
