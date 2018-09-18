from django import forms

from core.models import Room


class RoomChangeForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            'name',
            'description',
            'active',
            'color',
        )
