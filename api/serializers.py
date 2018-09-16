from rest_framework import serializers
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

    def validate(self, data):
        room = data.get('room')
        date = data.get('date')
        start = data.get('start')
        end = data.get('end')
        status = data.get('status')

        if start and end:
            if start > end:
                raise serializers.ValidationError('Start cannot be greater than end.')
            if room.booked(
                date=date,
                start=start,
                end=end
            ) and status == 'scheduled':
                raise serializers.ValidationError(
                    'Room {room} already booked in this period.'.format(
                        room=room.name
                    )
                )
