from django.shortcuts import render
from core.models import Room


def index(request):
    return render(request, 'core/index.html')


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'core/room_list.html', {
        'rooms': rooms,
    })
