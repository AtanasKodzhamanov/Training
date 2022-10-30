from django import forms
from django import forms
from examprep.web.models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = "__all__"

        