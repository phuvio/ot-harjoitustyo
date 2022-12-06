import unittest
from entities.participant import Patricipant
from services.participant_service import ParticipantService
from repositories.participant_repository import participant_repository


class FakeParticipantRepository:
    def __init__(self, participants=None):
        self.participants = participants or []

    def find_all(self):
        return self.participants

    def find_by_guide(self, guide):
        matching_participants = filter(
            lambda participant: participant.guide == guide,
            self.participants
        )

        matching_participants_list = list(matching_participants)

        return matching_participants_list

    def find_by_guide_and_travel(self, guide, travel):
        matching_participants = filter(
            lambda participant: participant.guide == guide and participant.travel == travel,
            self.participants
        )

        matching_participants_list = list(matching_participants)

        return matching_participants_list

    def find_by_name_and_guide(self, name, guide):
        matching_participants = filter(
            lambda participant: participant.name == name and participant.guide == guide,
            self.participants
        )

        matching_participants_list = list(matching_participants)

        return matching_participants_list

    def create(self, participant):
        self.participants.append(participant)

        return participant


class TestParticipantService(unittest.TestCase):
    def setUp(self):
        self.participant_service = ParticipantService(
            FakeParticipantRepository()
        )

        self._participant_mikko = Patricipant("Mikko", "Eka matka", "Jaana")
        self._participant_pekka = Patricipant("Pekka", "Eka matka", "Mari")
        self._participant_mari = Patricipant("Mari", "Eka matka", "Jaana")
        self._participant_ville = Patricipant("Ville", "Toka matka", "Jaana")

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
            "Mikko", "Eka matka", "Mari")

        participants = self.participant_service.get_participants_by_name_and_guide(
            self._participant_mikko.name, self._participant_mikko.guide)

        self.assertEqual(len(participants), 1)
        self.assertEqual(participants[0].name, self._participant_mikko.name)
