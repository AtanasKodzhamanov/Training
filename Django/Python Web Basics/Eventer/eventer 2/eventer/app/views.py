from django.shortcuts import render, redirect, get_object_or_404
from eventer.app.forms import ProfileForm, EventForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

from eventer.app.models import EventModel, ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def home(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'shared/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    events = EventModel.objects.all()

    context = {
        'profile': profile,
        'events': events
    }

    return render(request, 'events/dashboard.html', context)


def create_event(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.profile = get_profile()
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()

    context = {
        "profile": profile,
        'form': form,
    }
    return render(request, 'events/event-create.html', context)


def event_details(request, id):
    profile = get_profile()
    event = EventModel.objects.get(id=id)
    context = {
        'profile': profile,
        'event': event
    }
    return render(request, 'events/events-details.html', context)


def edit_event(request, id):
    profile = get_profile()
    event = get_object_or_404(EventModel, id=id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)

    context = {
        "profile": profile,
        'event': event,
        'form': form
    }
    return render(request, 'events/event-edit.html', context)


def delete_event(request, id):
    profile = get_profile()

    event = get_object_or_404(EventModel, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')
    context = {
        "profile": profile,
        'event': event
    }
    return render(request, 'events/events-delete.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    events_created = EventModel.objects.filter(profile=profile).count()

    context = {
        'profile': profile,
        'events_created': events_created,
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect after successful form submission
            return redirect('profile_details')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,  # Add the form to the context
    }
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        with transaction.atomic():
            # Delete all events associated with the profile
            EventModel.objects.filter(profile=profile).delete()

            # Delete the profile
            profile.delete()

        # Redirect to logout or another appropriate page
        return redirect('home')

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
