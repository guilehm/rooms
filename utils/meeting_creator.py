import datetime
import random

from django.core.exceptions import ValidationError
from django.utils import timezone
from model_mommy import mommy

from core.models import Meeting, Room

start_date = timezone.now()
end_date = start_date + timezone.timedelta(days=800)
room_list = Room.objects.all()

names = [
    'Alinhamento', 'Análise de fornecedor', 'Projeto ABC', 'Reunião com investidores', 'Reunião Criativa',
    'Reunião de Avaliação', 'Reunião de Tomada de Decisões', 'Reunião Informativa', 'Treinamento',
]


def random_date(start=start_date, end=end_date):
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def random_time():
    start = random.randint(0, 16)
    end = random.randint(start, 22)
    return str(start) + ':00', str(end) + ':00'


def create_meetings(rooms, quantity=1):
    meetings = []
    for i in range(0, quantity):
        name = random.choice(names)
        room = random.choice(rooms)
        date = random_date()
        start, end = random_time()
        try:
            meetings.append(mommy.make(
                Meeting,
                date=date,
                name=name,
                room=room,
                start=start,
                end=end
            ))
        except ValidationError:
            pass
    return meetings
