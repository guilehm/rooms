from django.core.exceptions import ValidationError
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField()
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '#{id} - {name}'.format(
            id=self.id,
            name=self.name
        )

    def get_meetings(self, date, start, end):
        meetings = self.meetings.filter(
            date=date,
            start__gte=start,
            end__lte=end
        )
        return meetings

    def booked(self, date, start, end):
        return self.get_meetings(
            date=date,
            start=start,
            end=end
        ).exists()


class Meeting(models.Model):
    SCHEDULED = 'scheduled'
    CANCELED = 'canceled'
    STATUS_CHOICES = (
        (SCHEDULED, 'Scheduled'),
        (CANCELED, 'Canceled'),
    )
    room = models.ForeignKey(
        'core.Room',
        related_name='meetings',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=SCHEDULED,
        db_index=True
    )
    date = models.DateField(db_index=True)
    start = models.TimeField(db_index=True)
    end = models.TimeField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start and self.end:
            if self.start > self.end:
                raise ValidationError('Start cannot be greater than end.')
            if self.room.booked(
                date=self.date,
                start=self.start,
                end=self.end
            ) and self.status == self.SCHEDULED:
                raise ValidationError(
                    'Room {room} already booked in this period.'.format(
                        room=self.room.name
                    )
                )
