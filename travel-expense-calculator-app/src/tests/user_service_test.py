import unittest
from entities.user import User
from services.user_service import (
    UserService,
    InvalidCredentialsError,
    UsernameExistsError
)
from repositories.user_repository import user_repository


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(
            user_repository
        )

        user_repository.delete_all()

        self._user_jaana = User('Jaana', '1234')
        self._user_mari = User('Mari', 'abc')

    def login_user(self, user):
        self.user_service.create_user(user.username, user.password)

    def test_login_with_valid_username_and_password(self):
        self.user_service.create_user(
            self._user_jaana.username,
            self._user_jaana.password
        )

        user = self.user_service.login(
            self._user_jaana.username,
            self._user_jaana.password
        )

        self.assertEqual(user.username, self._user_jaana.username)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.user_service.login('testing', 'invalid')
        )

    def test_get_current_user(self):
        self.login_user(self._user_jaana)

        current_user = self.user_service.get_current_user()

        self.assertEqual(current_user.username, self._user_jaana.username)

    def test_create_user_with_non_existing_username(self):
        username = self._user_jaana.username
        password = self._user_jaana.password

        self.user_service.create_user(username, password)

        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self._user_jaana.username

        self.user_service.create_user(username, 'something')

        self.assertRaises(
            UsernameExistsError,
            lambda: self.user_service.create_user(username, 'random')
        )

    def test_logout_current_user(self):
        self.login_user(self._user_jaana)

        self.user_service.logout()

        current_user = self.user_service.get_current_user()

        self.assertIsNone(current_user)

    def tearDown(self):
        user_repository.delete_all()
