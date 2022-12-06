import unittest
from repositories.participant_repository import participant_repository
from entities.participant import Patricipant


class TestParticipantRepository(unittest.TestCase):
    def setUp(self):
        participant_repository.delete_all()

        self._participant_mikko = Patricipant("Mikko", "Eka matka", "Jaana")
        self._participant_pekka = Patricipant("Pekka", "Eka matka", "Mari")
        self._participant_mari = Patricipant("Mari", "Eka matka", "Jaana")
        self._participant_ville = Patricipant("Ville", "Toka matka", "Jaana")

    def test_create_one_participant(self):
        participant_repository.create(self._participant_mikko)
        participants = participant_repository.find_all()

        self.assertEqual(len(participants), 1)
        self.assertEqual(participants[0].name, self._participant_mikko.name)

    def test_find_participants_by_guide(self):
        participant_repository.create(self._participant_mikko)
        participant_repository.create(self._participant_pekka)
        participant_repository.create(self._participant_mari)
        participant_repository.create(self._participant_ville)
        participants = participant_repository.find_by_guide("Jaana")

        self.assertEqual(len(participants), 3)
        self.assertEqual(participants[0].name, self._participant_mikko.name)
        self.assertEqual(participants[1].name, self._participant_mari.name)
        self.assertEqual(participants[2].name, self._participant_ville.name)

    def test_find_participants_guide_and_travel(self):
        participant_repository.create(self._participant_mikko)
        participant_repository.create(self._participant_pekka)
        participant_repository.create(self._participant_mari)
        participant_repository.create(self._participant_ville)
        participants = participant_repository.find_by_guide_and_travel(
            "Jaana", "Eka matka")

        self.assertEqual(len(participants), 2)
        self.assertEqual(participants[0].name, self._participant_mikko.name)
        self.assertEqual(participants[1].name, self._participant_mari.name)

    def test_find_participants_name_and_guide(self):
        participant_repository.create(self._participant_mikko)
        participant_repository.create(self._participant_pekka)
        participant_repository.create(self._participant_mari)
        participant_repository.create(self._participant_ville)
        participant_repository.create(
            Patricipant("Mikko", "Eka matka", "Mari"))
        participants = participant_repository.find_by_name_and_guide(
            "Mikko", "Jaana")

        self.assertEqual(participants.name, self._participant_mikko.name)
        self.assertEqual(participants.guide, self._participant_mikko.guide)
