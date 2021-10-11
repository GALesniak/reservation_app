from django import forms

from .models import Room, Booking
from django.forms.widgets import DateInput


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'capacity', 'projector', 'date_now']
        labels = {
            'room_name': 'Conference Room Name',
            'capacity': 'Capacity of the room',
            'projector': 'Projector Availability',
            'date_now': "Insertion date",

        }
        widgets = {
            'date_now': DateInput(attrs={'type': 'date'}),

        }


class BookingForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d", ])

