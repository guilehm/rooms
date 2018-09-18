from django import forms

from core.models import Meeting, Room


class RoomChangeForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            'name',
            'description',
            'color',
        )


class MeetingChangeForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Meeting
        fields = (
            'room',
            'name',
            'description',
            'status',
            'date',
            'start',
            'end',
        )
