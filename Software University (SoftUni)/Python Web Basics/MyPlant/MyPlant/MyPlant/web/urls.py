from django.urls import path
from .views import home_view, profile_create_view, catalogue_view, plant_create_view, plant_details_view, plant_edit_view, plant_delete_view, profile_details_view, profile_edit_view, profile_delete_view

urlpatterns = [ 
    path('', home_view, name="home"),
    path('profile/create/', profile_create_view, name="profile_create"),
    path('catalogue/', catalogue_view, name="catalogue"),
    path('create/', plant_create_view, name="plant_create"),
    path('details/<int:plant_pk>/', plant_details_view, name="plant_details"),
    path('edit/<int:plant_pk>/', plant_edit_view, name="plant_edit"),
    path('delete/<int:plant_pk>/', plant_delete_view, name="plant_delete"),
    path('profile/details/', profile_details_view, name="profile_details"),
    path('profile/edit/', profile_edit_view, name="profile_edit"),
    path('profile/delete/', profile_delete_view, name="profile_delete"),

]

