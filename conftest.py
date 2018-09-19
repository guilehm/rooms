import pytest
from model_mommy import mommy
from rest_framework.test import APIClient


@pytest.fixture
def public_client():
    client = APIClient()
    return client


@pytest.fixture
def room_one():
    return mommy.make(
        'core.Room',
        name='São Paulo',
        slug='sao-paulo',
        description='Sala para até 10 pessoas',
        color='red',
    )


@pytest.fixture
def room_two():
    return mommy.make('core.Room')


@pytest.fixture
def meeting_one(room_one):
    return mommy.make(
        'core.Meeting',
        name='Reunião com investidores',
        description='Apresentação de resultados do trimestre',
        room=room_one,
        date='2018-12-26',
        status='scheduled',
        start='14:00',
        end='16:00',
    )


@pytest.fixture
def meeting_two(room_two):
    return mommy.make(
        'core.Meeting',
        room=room_two,
        date='2018-12-26',
        status='scheduled',
        start='14:00',
        end='16:00',
    )
