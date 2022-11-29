from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UserService:
    """Matkoihin liittyvästä sovelluslogiikasta vastaava luokka"""

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori. Luo uuden matkojen sovelluslogiikasta vastaavan palvelun

        Args:
            user_repository: Olio, jolla on UserResopitory-luokkaa vastaavat metodit
        """
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa käyttäjän sisään

        Args:
            username: Merkkijono, joka kuvastaa käyttäjän käyttäjätunnusta
            password: Merkkijono, joka kuvastaa käyttäjän salasanaa
            login:
                Vapaaehtoinen, oletusarvo True
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen

        Raises:
            UserNameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä

        Returns:
            Luotu käyttäjä User-olion muodossa
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(
                f"Käyttäjätunnus {username} on jo käytössä")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään

        Args:
            username: Merkkijono, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta
            password: Merkkijono, joka kuvaa kirjautuvan käyttäjän salasanaa

        Returns:
            Kirjautunut käyttäjä User-olion muodossa

        Raises:
            InvalidCredentialsErros:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää

        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError(
                "Virheellinen käyttäjätunnus tai salasana")

        self._user = user

        return user

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän

        Returns:
            Kirjautunut käyttäjä User-olion muodossa
        """

        return self._user

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos"""

        self._user = None

    def get_users(self):
        """Palauttaa kaikki käyttäjät

        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """

        return self._user_repository.find_all()


user_service = UserService()
