from django.shortcuts import render

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
