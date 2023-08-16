from django import forms

from eventer.app.models import EventModel, ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name',
                  'email', 'profile_picture', 'password']


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['event_name', 'category',
                  'description', 'date', 'event_image']
