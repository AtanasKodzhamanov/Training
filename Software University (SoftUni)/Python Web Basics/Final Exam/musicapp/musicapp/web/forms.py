from django import forms

from musicapp.web.models import Profile, Album

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        #add placeholders
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }

class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        #add placeholders
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
        }