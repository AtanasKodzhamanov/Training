from django.urls import path, include

from examprep.web.views import index, add_profile, delete_album, details_album, add_album, edit_album, delete_profile, details_profile

'''
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page
'''

urlpatterns = (
    path("", index, name="index"),
    path("album/", include([
        path("details/<int:pk>/", details_album, name="details_album"),
        path("add/", add_album, name="add_album"),
        path("edit/<int:pk>/", edit_album, name="edit_album"),
        path("delete/<int:pk>/", delete_album, name="delete_album"),
    ])),
    path("profile/", include([
        path("add/",add_profile, name="add_profile"),
        path("details/", details_profile, name="details_profile"),
        path("delete/", delete_profile, name="delete_profile"),
    ])),
)