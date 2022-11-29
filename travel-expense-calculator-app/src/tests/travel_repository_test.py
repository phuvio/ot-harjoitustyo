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
        travel = travel_repository.find_by_name("Eka matka")

        self.assertEqual(travel.name, self._travel_a.name)
