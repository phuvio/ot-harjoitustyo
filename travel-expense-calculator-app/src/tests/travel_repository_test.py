import unittest
from repositories.travel_repository import travel_repository
from entities.travel import Travel


class TestTravelRepository(unittest.TestCase):
    def setUp(self):
        travel_repository.delete_all()

        self.travel_a = Travel({
            "name": "Eka matka",
            "participants": "Maisa"
        })
        self.travel_b = Travel({
            "name": "Toka matka",
            "participants": "Topi"
        })

    def test_create(self):
        travel_repository.create(self.travel_a)
        travels = travel_repository.find_all()

        self.assertEqual(len(travels, 1))
        self.assertEqual(travels[0].name, self.travel_a.name)
