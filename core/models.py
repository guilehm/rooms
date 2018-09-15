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


class Meeting(models.Model):
    room = models.ForeignKey(
        'core.Room',
        related_name='meetings',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
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
