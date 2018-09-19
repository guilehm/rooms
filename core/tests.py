import pytest
from django.urls import reverse

from rest_framework import status


@pytest.mark.django_db
class TestRoomCreation:

    @pytest.fixture
    def rooms_endpoint(self):
        return reverse('api:room-list')

    @pytest.fixture
    def payload_room_creation(self):
        return {
            'name': 'Sala Brasil',
            'slug': 'sala-brasil',
            'description': 'sala com televisão para até 5 pessoas',
            'color': 'green',
        }

    def test_should_create_room(self, rooms_endpoint, public_client, payload_room_creation):
        response = public_client.post(
            rooms_endpoint, data=payload_room_creation, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
