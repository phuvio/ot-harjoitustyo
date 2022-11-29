import unittest
from entities.travel import Travel
from entities.user import User
from services.travel_service import TravelService


class FakeTravelRepository:
    def __init__(self, travels=None):
        self.travels = travels or []

    def find_all(self):
        return self.travels

    def find_by_name(self, name):
        user_travels = filter(
            lambda travel: travel.name == name,
            self.travels
        )

        return list(user_travels)

    def find_by_participant(self, participant):
        user_travels = filter(
            lambda travel: travel.participants == participant,
            self.travels
        )

        return list(user_travels)

    def create(self, travel):
        self.travels.append(travel)

        return travel


class TestTravelService(unittest.TestCase):
    def setUp(self):
        self.travel_service = TravelService(
            FakeTravelRepository(),
        )

        self._travel_eka = Travel('Eka matka', 'Jaana')
        self._travel_toka = Travel('Toka matka', 'Mari')
        self._user_jaana = User('Jaana', '1234')

    def test_create_travel(self):
        name = self._travel_eka.name
        participants = self._travel_eka.participants

        self.travel_service.create_travel(name, participants)
        travels = self.travel_service.get_all_travels()

        self.assertEqual(len(travels), 1)
        self.assertEqual(travels[0].name, self._travel_eka.name)

    def test_create_two_travels(self):
        name = self._travel_eka.name
        participants = self._travel_eka.participants

        self.travel_service.create_travel(name, participants)

        name = self._travel_toka.name
        participants = self._travel_toka.participants

        self.travel_service.create_travel(name, participants)

        travels = self.travel_service.get_all_travels()

        self.assertEqual(len(travels), 2)
        self.assertEqual(travels[0].name, self._travel_eka.name)
        self.assertEqual(travels[1].name, self._travel_toka.name)

    def test_travels_by_name(self):
        self.travel_service.create_travel(
            self._travel_eka.name, self._travel_eka.participants)
        self.travel_service.create_travel(
            self._travel_toka.name, self._travel_toka.participants)

        travel = self.travel_service.get_users_travels(self._travel_eka.participants)

        self.assertEqual(len(travel), 1)
        self.assertEqual(travel[0].name, self._travel_eka.name)
