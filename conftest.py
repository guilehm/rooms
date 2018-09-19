import pytest
from model_mommy import mommy
from rest_framework.test import APIClient
from django.utils import timezone


@pytest.fixture
def public_client():
    client = APIClient()
    return client


@pytest.fixture
def room_one():
    return mommy.make('core.Room')


@pytest.fixture
def room_two():
    return mommy.make('core.Room')


@pytest.fixture
def meeting_one(room_one):
    return mommy.make(
        'core.Meeting',
        room=room_one,
        date=timezone.now().date(),
        status='scheduled',
        start=timezone.now(),
        end=timezone.now() + timezone.timedelta(minutes=100),
    )


@pytest.fixture
def meeting_two(room_two):
    return mommy.make(
        'core.Meeting',
        room=room_two,
        status='scheduled',
        date=timezone.now().date(),
        start=timezone.now(),
        end=timezone.now() + timezone.timedelta(minutes=240),
    )


