from django.shortcuts import redirect, render
from MyPlant.web.models import Plant, Profile
from MyPlant.web.forms import PlantForm, ProfileForm, PlantDeleteForm, ProfileDeleteForm

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None 

def home_view(request):
    profile = get_profile()
    context={
        "profile": profile,
    }

    return render(request, "home-page.html", context)

def catalogue_view(request):
    profile = get_profile()
    if profile is None: 
        return redirect("profile_create")
    context = {
        "plants": Plant.objects.all(),
    }
    return render(request, "catalogue.html", context)

def profile_create_view(request):
    if request.method == "GET":
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "create-profile.html", context)

def profile_details_view(request):
    profile = get_profile()
    plant_count = Plant.objects.count()
    stars = 0
    if plant_count <3:
        stars=plant_count
    else:
        stars=3
    context = {
        "profile": profile,
        "stars": stars,
    }
    return render(request, "profile-details.html", context)

def profile_edit_view(request):
    profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "edit-profile.html", context)

def profile_delete_view(request):
    profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileDeleteForm(instance= profile)
    else:
        form = ProfileDeleteForm(request.POST, instance= profile)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "delete-profile.html", context)

def plant_create_view(request):
    if request.method == "GET":
        form = PlantForm()
    else:
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "form": form,
    }
    return render(request, "create-plant.html", context)

def plant_details_view(request, plant_pk):
    plant = Plant.objects.filter(pk=plant_pk).get()

    context = {
        "plant": plant,
    }
    return render(request, "plant-details.html", context)

def plant_edit_view(request, plant_pk):
    plant = Plant.objects.filter(pk=plant_pk).get()
    if request.method == "GET":
        form = PlantForm(instance=plant)
    else:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "plant": plant,
        "form": form,
    }
    return render(request, "edit-plant.html", context)

def plant_delete_view(request, plant_pk):
    plant = Plant.objects.filter(pk=plant_pk).get()
    if request.method == "GET":
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "plant": plant,
        "form": form,
    }
    return render(request, "delete-plant.html", context)




