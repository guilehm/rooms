from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from core.forms import MeetingChangeForm, RoomChangeForm
from core.models import Meeting, Room


def index(request):
    return render(request, 'core/index.html')


def room_list(request):
    rooms = Room.objects.order_by('name')
    return render(request, 'core/room_list.html', {
        'rooms': rooms,
    })


def meeting_list(request):
    meetings = Meeting.objects.prefetch_related(
        'room',
    ).order_by('date', 'start')
    return render(request, 'core/meeting_list.html', {
        'meetings': meetings,
    })


def meeting_calendar(request):
    meetings = Meeting.objects.prefetch_related(
        'room',
    ).order_by('date', 'start')
    return render(request, 'core/meeting_calendar.html', {
        'meetings': meetings,
    })


def room_add(request):
    form = RoomChangeForm()
    if request.method == 'POST':
        form = RoomChangeForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.slug = slugify(room.name)
            room.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                extra_tags='success',
                message='Sala {name} criada com sucesso.'.format(
                    name=room.name
                )
            )
            return redirect('core:room-list')
    return render(request, 'core/room_change.html', {
        'form': form,
    })


def room_change(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = RoomChangeForm(instance=room)
    if request.method == 'POST':
        form = RoomChangeForm(data=request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.slug = slugify(room.name)
            room.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                extra_tags='success',
                message='Sala {name} editada com sucesso.'.format(
                    name=room.name
                )
            )
            return redirect('core:room-list')
    return render(request, 'core/room_change.html', {
        'form': form,
        'room': room,
    })


def meeting_add(request):
    rooms = Room.objects.all()
    form = MeetingChangeForm()
    if request.method == 'POST':
        form = MeetingChangeForm(request.POST)
        if form.is_valid():
            meeting = form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                extra_tags='success',
                message='Reunião {name} criada com sucesso.'.format(
                    name=meeting.name
                )
            )
            return redirect('core:meeting-list')
    return render(request, 'core/meeting_change.html', {
        'form': form,
        'rooms': rooms,
    })


def meeting_change(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    rooms = Room.objects.all()
    form = MeetingChangeForm(instance=meeting)
    if request.method == 'POST':
        form = MeetingChangeForm(data=request.POST, instance=meeting)
        if form.is_valid():
            meeting.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                extra_tags='success',
                message='Reunião {name} editada com sucesso.'.format(
                    name=meeting.name
                )
            )
            return redirect('core:meeting-list')
    return render(request, 'core/meeting_change.html', {
        'form': form,
        'rooms': rooms,
        'meeting': meeting,
    })
