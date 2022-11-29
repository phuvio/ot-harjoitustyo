import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self._user_jaana = User('Jaana', '1234')
        self._user_mari = User('Mari', '1234')

    def test_create_new_user(self):
        user_repository.create(self._user_jaana)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self._user_jaana.username)

    def test_create_two_new_users(self):
        user_repository.create(self._user_mari)
        user_repository.create(self._user_jaana)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self._user_mari.username)
        self.assertEqual(users[1].username, self._user_jaana.username)

    def test_create_two_new_users_and_search_for_one_username(self):
        user_repository.create(self._user_mari)
        user_repository.create(self._user_jaana)
        users = user_repository.find_by_username('Jaana')

        self.assertEqual(users.username, self._user_jaana.username)
