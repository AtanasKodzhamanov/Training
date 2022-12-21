from django.urls import path

from musicapp.web.views import index, details_album, add_album, edit_album, delete_album, details_profile, delete_profile

urlpatterns = [
    path("", index, name="index"),
    path("album/details/<int:pk>/", details_album, name="details_album"),
    path("album/add/", add_album, name="add_album"),
    path("album/edit/<int:pk>/", edit_album, name="edit_album"),
    path("album/delete/<int:id>/", delete_album, name="delete_album"),
    path("profile/details/", details_profile, name="details_profile"),
    path("profile/delete/", delete_profile, name="delete_profile"),
]
