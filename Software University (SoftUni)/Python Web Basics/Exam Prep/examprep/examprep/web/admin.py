from django.contrib import admin

from examprep.web.models import Profile, Album

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass 

@admin.register(Album)
class AlbumAmdin(admin.ModelAdmin):
    pass

# Register your models here.
