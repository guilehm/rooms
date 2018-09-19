from copy import deepcopy

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
            "name": "Sala Brasil",
            "slug": "sala-brasil",
            "description": "sala com televisão para até 5 pessoas",
            "color": "green",
        }

    def test_should_create_room(self, rooms_endpoint, public_client, payload_room_creation):
        response = public_client.post(
            rooms_endpoint, data=payload_room_creation, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestRoomPayload:

    @pytest.fixture
    def rooms_endpoint(self):
        return reverse('api:room-list')

    @pytest.fixture
    def payload_room_list(self, room_one):
        return [
            {
                "id": 1,
                "name": "São Paulo",
                "slug": "sao-paulo",
                "description": "Sala para até 10 pessoas",
                "color": "red",
            }
        ]

    def test_should_return_right_payload(self, rooms_endpoint, public_client, payload_room_list):
        response = public_client.get(rooms_endpoint)
        json_response = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert json_response == payload_room_list


@pytest.mark.django_db
class TestMeetingCreation:

    @pytest.fixture
    def meeting_endpoint(self):
        return reverse('api:meeting-list')

    @pytest.fixture
    def payload_meeting_creation(self):
        return {
            "name": "Apresentação de projeto",
            "room": 1,
            "description": "apresentação do projeto para o cliente",
            "status": "scheduled",
            "date": "26/12/2018",
            "start": "14:00",
            "end": "16:00"
        }

    @pytest.fixture
    def payload_meeting_creation_with_different_date_format(self):
        return {
            "name": "Apresentação de projeto",
            "room": 1,
            "description": "apresentação do projeto para o cliente",
            "status": "scheduled",
            "date": "26-12-2018",
            "start": "14:00",
            "end": "16:00"
        }

    @pytest.fixture
    def payload_meeting_creation_with_different_time_format(self):
        return {
            "name": "Apresentação de projeto",
            "room": 1,
            "description": "apresentação do projeto para o cliente",
            "status": "scheduled",
            "date": "26-12-2018",
            "start": "14:00:00",
            "end": "16:00:00"
        }

    @pytest.fixture
    def payload_conflicting_meeting_creation(self, payload_meeting_creation):
        payload = deepcopy(payload_meeting_creation)
        payload['start'] = '12:00'
        payload['end'] = '18:00'
        return payload

    @pytest.fixture
    def payload_conflicting_meeting_creation_with_canceled_status(self, payload_conflicting_meeting_creation):
        payload = deepcopy(payload_conflicting_meeting_creation)
        payload['status'] = 'canceled'
        return payload

    @pytest.fixture
    def payload_end_greater_than_start_meeting_creation(self, payload_meeting_creation):
        payload = deepcopy(payload_meeting_creation)
        payload['start'] = '18:00'
        payload['end'] = '10:00'
        return payload

    def test_should_create_meeting(
            self, meeting_endpoint, public_client, payload_meeting_creation, room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_meeting_creation, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_create_meeting_with_different_date_format(
            self, meeting_endpoint, public_client, payload_meeting_creation_with_different_date_format, room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_meeting_creation_with_different_date_format, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_create_meeting_with_different_time_format(
            self, meeting_endpoint, public_client, payload_meeting_creation_with_different_time_format, room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_meeting_creation_with_different_time_format, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_not_create_meeting_with_conflicting_time(
            self, meeting_endpoint, public_client, payload_conflicting_meeting_creation, meeting_one, room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_conflicting_meeting_creation, format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['non_field_errors'][0] == 'Room {name} already booked in this period.'.format(
            name=room_one.name
        )

    def test_should_create_meeting_with_conflicting_time_but_canceled_status(
            self,
            meeting_endpoint,
            public_client,
            payload_conflicting_meeting_creation_with_canceled_status,
            meeting_one,
            room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_conflicting_meeting_creation_with_canceled_status, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_not_create_meeting_with_end_greater_than_start(
            self, meeting_endpoint, public_client, payload_end_greater_than_start_meeting_creation, room_one
    ):
        response = public_client.post(
            meeting_endpoint, data=payload_end_greater_than_start_meeting_creation, format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['non_field_errors'][0] == 'Start cannot be greater than end.'


@pytest.mark.django_db
class TestMeetingPayload:

    @pytest.fixture
    def meeting_endpoint(self):
        return reverse('api:meeting-list')

    @pytest.fixture
    def payload_meeting_list(self, meeting_one):
        return [
            {
                "id": 1,
                "name": "Reunião com investidores",
                "room": 1,
                "description": "Apresentação de resultados do trimestre",
                "status": "scheduled",
                "date": "26-12-2018",
                "start": "14:00:00",
                "end": "16:00:00",
            }
        ]

    def test_should_return_right_payload(self, meeting_endpoint, public_client, payload_meeting_list):
        response = public_client.get(meeting_endpoint)
        json_response = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert json_response == payload_meeting_list
