import unittest
from repositories.travel_repository import travel_repository
from entities.travel import Travel


class TestTravelRepository(unittest.TestCase):
    def setUp(self):
        travel_repository.delete_all()

        self._travel_a = Travel("Eka matka", "Maisa")
        self._travel_b = Travel("Toka matka", "Topi")

    def test_create_one_travel(self):
        travel_repository.create(self._travel_a)
        travels = travel_repository.find_all()

        self.assertEqual(len(travels), 1)
        self.assertEqual(travels[0].name, self._travel_a.name)

    def test_create_two_travels(self):
        travel_repository.create(self._travel_a)
        travel_repository.create(self._travel_b)
        travels = travel_repository.find_all()

        self.assertEqual(len(travels), 2)
        self.assertEqual(travels[0].name, self._travel_a.name)
        self.assertEqual(travels[1].name, self._travel_b.name)

    def test_find_travel_by_name(self):
        travel_repository.create(self._travel_a)
        travel = travel_repository.find_by_name(self._travel_a.name)

        self.assertEqual(travel.name, self._travel_a.name)

    def test_find_travels_by_guide(self):
        travel_repository.create(self._travel_a)
        travel_repository.create(self._travel_b)

        travel = travel_repository.find_by_guide(self._travel_a.guide)

        self.assertEqual(len(travel), 1)

        travel_repository.create(Travel("Kolmas matka", self._travel_a.guide))

        travel = travel_repository.find_by_guide(self._travel_a.guide)

        self.assertEqual(len(travel), 2)
        self.assertEqual(travel[1].name, "Kolmas matka")
