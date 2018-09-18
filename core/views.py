from django.shortcuts import get_object_or_404, render, redirect
from django.utils.text import slugify
from django.contrib import messages

from core.forms import RoomChangeForm
from core.models import Meeting, Room


def index(request):
    return render(request, 'core/index.html')


def room_list(request):
    rooms = Room.objects.order_by('name')
    return render(request, 'core/room_list.html', {
        'rooms': rooms,
    })


def meeting_list(request):
    meetings = Meeting.objects.order_by('date', 'start')
    return render(request, 'core/meeting_list.html', {
        'meetings': meetings,
    })


def meeting_calendar(request):
    meetings = Meeting.objects.order_by('date', 'start')
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
