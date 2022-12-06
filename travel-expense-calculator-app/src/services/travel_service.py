from entities.travel import Travel
from repositories.travel_repository import (
    travel_repository as default_travel_repository)


class TravelService:
    """Matkoihin liittyvästä sovelluslogiikasta vastaava luokka"""

    def __init__(self, travel_repository=default_travel_repository):
        """Luokan konstruktori. Luo uuden matkoihin liittyvästä sovelluslogiikasta
           vastaavan palvelun

        Args:
            travel: Valittu matka Travel-olion muodossa
            travel_repository: Olio, jolla on TravelRepository-luokkaa vastaavat metodit
        """

        self._travel = None
        self._travel_repository = travel_repository

    def create_travel(self, name, guide):
        """Luo uuden matkan

        Args:
            name: Merkkijono, joka kuvastaa matkan nimeä
            guide: Merkkijono, joka kuvastaa matkan matkanjohtajan nimeä

        Returns:
            Luotu matkustaja Travel-olion muodossa
        """

        travel = Travel(name, guide)

        return self._travel_repository.create(travel)

    def get_users_travels(self, username):
        """Palauttaa matkanjohtajaan liittyvät matkat

        Args:
            username: Merkkijono, joka kuvastaa matkan matkanjohtajan nimeä

        Returns:
            Lista kirjautuneeseen käyttäjään liittyvistä matkoista Travel-olioiden muodossa
        """

        travels = self._travel_repository.find_by_guide(username)

        return list(travels)

    def get_all_travels(self):
        """Palauttaa kaikki matkat

        Returns:
            Travel-oliota sisältävä lista kaikista käyttäjistä.
        """

        return self._travel_repository.find_all()

    def get_current_travel(self):
        """Palauttaa nykyisen matkan

        Returns:
            Palauttaa valitun matkan Travel-olion muodossa
        """

        return self._travel


travel_service = TravelService()
