from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "home_with_profile.html")

def details_album(request, pk):
    return render(request, "album_details.html")  

def add_album(request):
    return render(request, "add_album.html")

def edit_album(request, pk):
    return render(request, "edit_album.html")

def delete_album(request, id):
    return render(request, "delete_album.html")

def details_profile(request):
    return render(request, "profile_details.html")

def delete_profile(request):
    return render(request, "delete_profile.html")
