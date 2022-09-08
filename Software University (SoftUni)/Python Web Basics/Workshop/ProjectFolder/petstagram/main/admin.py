from django.contrib import admin

from ProjectFolder.petstagram.main.models import Pet
from petstagram.main.models import Profile 

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass 

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass