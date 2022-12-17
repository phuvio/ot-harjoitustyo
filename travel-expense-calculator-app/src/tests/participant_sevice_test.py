import unittest
from entities.participant import Patricipant
from services.participant_service import ParticipantService
from repositories.participant_repository import participant_repository


class TestParticipantService(unittest.TestCase):
    def setUp(self):
        self.participant_service = ParticipantService(
            participant_repository
        )
        participant_repository.delete_all()

        self._participant_mikko = Patricipant("Mikko", 3, "Jaana")
        self._participant_pekka = Patricipant("Pekka", 2, "Mari")
        self._participant_mari = Patricipant("Mari", 3, "Jaana")
        self._participant_ville = Patricipant("Ville", 4, "Jaana")

    def test_create_participant(self):
        name = self._participant_mikko.name
        travel = self._participant_mikko.travel
        guide = self._participant_mikko.guide

        self.participant_service.create_participant(name, travel, guide)
        participants = self.participant_service.get_all_participants()

        self.assertEqual(len(participants), 1)
        self.assertEqual(participants[0].name, self._participant_mikko.name)

    def test_participants_by_guide(self):
        self.participant_service.create_participant(
            self._participant_mari.name, self._participant_mari.travel, self._participant_mari.guide)
        self.participant_service.create_participant(
            self._participant_mikko.name, self._participant_mikko.travel, self._participant_mikko.guide)
        self.participant_service.create_participant(
            self._participant_pekka.name, self._participant_pekka.travel, self._participant_pekka.guide)
        self.participant_service.create_participant(
            self._participant_ville.name, self._participant_ville.travel, self._participant_ville.guide)

        participants = self.participant_service.get_participants_by_guide(
            self._participant_mikko.guide)

        self.assertEqual(len(participants), 3)
        self.assertEqual(participants[0].name, self._participant_mari.name)
        self.assertEqual(participants[1].name, self._participant_mikko.name)
        self.assertEqual(participants[2].name, self._participant_ville.name)

    def test_participants_by_guide_and_travel(self):
        self.participant_service.create_participant(
            self._participant_mari.name, self._participant_mari.travel, self._participant_mari.guide)
        self.participant_service.create_participant(
            self._participant_mikko.name, self._participant_mikko.travel, self._participant_mikko.guide)
        self.participant_service.create_participant(
            self._participant_pekka.name, self._participant_pekka.travel, self._participant_pekka.guide)
        self.participant_service.create_participant(
            self._participant_ville.name, self._participant_ville.travel, self._participant_ville.guide)

        participants = self.participant_service.get_participants_by_guide_and_travel(
            self._participant_mikko.guide, self._participant_mikko.travel)

        self.assertEqual(len(participants), 2)
        self.assertEqual(participants[0].name, self._participant_mari.name)
        self.assertEqual(participants[1].name, self._participant_mikko.name)

    def test_participants_by_name_and_guide(self):
        self.participant_service.create_participant(
            self._participant_mari.name, self._participant_mari.travel, self._participant_mari.guide)
        self.participant_service.create_participant(
            self._participant_mikko.name, self._participant_mikko.travel, self._participant_mikko.guide)
        self.participant_service.create_participant(
            "Mikko", 5, "Mari")

        participants = self.participant_service.get_participants_by_name_and_guide(
            self._participant_mikko.name, self._participant_mikko.guide)

        self.assertEqual(participants.name, self._participant_mikko.name)

    def tearDown(self):
        participant_repository.delete_all()
