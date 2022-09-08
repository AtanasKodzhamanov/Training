from django.urls import path

from . import views 

urlspatterns=[
    path("home", views.home),
    path("authorized", views.authorized)
]