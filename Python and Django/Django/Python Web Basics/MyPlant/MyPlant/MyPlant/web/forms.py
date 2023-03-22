from django import forms

from MyPlant.web.models import Plant, Profile 

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class PlantDeleteForm(PlantForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__set_disabled_fields()

    def save(self,commit=True):
        if commit:
            self.instance.delete()
        return self.instance
    
    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"

class ProfileDeleteForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ()    
    
    def save(self,commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    