from django.shortcuts import redirect, render

from musicapp.web.models import Profile, Album
from musicapp.web.forms import ProfileCreateForm, AlbumCreateForm

# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None 

def index(request):
    profile = get_profile()
    if profile is None: 
        return redirect("add_profile")

    context = {
        "albums": Album.objects.all(),
    }
    return render(request, "home-with-profile.html", context)

def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        "album": album,
    }
    return render(request, "album-details.html", context)  

def add_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "add-album.html", context)

def edit_album(request, pk):
    return render(request, "edit-album.html")

def delete_album(request, id):
    return render(request, "delete-album.html")

def details_profile(request):
    return render(request, "profile-details.html")

def delete_profile(request):
    return render(request, "delete-profile.html")

def add_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else: 
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "home-no-profile.html", context)