from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('details/<int:id>/', views.event_details, name='event_details'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]
