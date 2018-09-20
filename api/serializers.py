import logging

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Meeting, Room

logger = logging.getLogger('rooms')


class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'color',
        )

    def create(self, validated_data):
        logger.info('Creating room "{name}".'.format(
            name=validated_data.get('name')
        ))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logger.info('Updating room "{name}".'.format(
            name=instance.name
        ))
        return super().update(instance, validated_data)


class MeetingSerializer(ModelSerializer):
    date = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y', '%d/%m/%Y'])

    class Meta:
        model = Meeting
        fields = (
            'id',
            'name',
            'room',
            'description',
            'status',
            'date',
            'start',
            'end',
        )

    def create(self, validated_data):
        logger.info(
            'Creating meeting "{meeting_name}" for room "{room_name}".'.format(
                meeting_name=validated_data.get('name'),
                room_name=validated_data.get('room').name
            )
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logger.info(
            'Updating meeting "{meeting_name}" for room "{room_name}".'.format(
                meeting_name=validated_data.get('name'),
                room_name=validated_data.get('room').name
            )
        )
        return super().update(instance, validated_data)

    def validate(self, data):
        room = data.get('room')
        date = data.get('date')
        start = data.get('start')
        end = data.get('end')
        status = data.get('status')
        meeting_id = self.context.get('request').data.get('id')

        if start and end:
            if start > end:
                logger.error(
                    'Problem trying to validate meeting. Start cannot be greater than end.',
                )
                raise serializers.ValidationError('Start cannot be greater than end.')
            if room.conflict(
                date=date,
                start=start,
                end=end,
                meeting_id=meeting_id,
            ) and status == 'scheduled':
                logger.error(
                    'Problem trying to validate meeting. Room {room} already booked in this period.'.format(
                        room=room.name,
                    )
                )
                raise serializers.ValidationError(
                    'Room {room} already booked in this period.'.format(
                        room=room.name
                    )
                )
        return data
