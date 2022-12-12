from entities.participant import Patricipant
from repositories.participant_repository import (
    participant_repository as default_participant_repository)


class ParticipantExistsError(Exception):
    pass


class ParticipantService:
    """Matkustajiin liittyvästä sovelluslogiikasta vastaava luokka"""

    def __init__(self, participant_repository=default_participant_repository):
        """Luokan konstruktori. Luo uuden matkustajiin liittyvästä sovelluslogiikasta
           vastaavan palvelun

        Args:
            participant_repository: Olio, jolla on ParticipantRepository-luokkaa vastaavat metodit
        """

        self._participant = None
        self._participant_repository = participant_repository

    def create_participant(self, name, travel, guide):
        """Luo uuden matkustajan

        Args:
            name: Merkkijono, joka kuvastaa matkustajan nimeä
            travel: Mekkijono, joka kuvastaa matkustajan matkaa
            guide: Merkkijono, joka kuvastaa matkustajan matkanjohtajaa

        Returns:
            Luotu matkustaja Participant-olion muodossa
        """

        participant = Patricipant(name, travel, guide)

        return self._participant_repository.create(participant)

    def get_participants_by_guide(self, guide):
        """Palauttaa matkanjohtajaan liittyvät matkustajat

        Args:
            guide: Merkkijono, joka kuvastaa matkustajan matkanjohtajaa

        Returns:
            Lista kirjautuneeseen käyttäjään liittyvistä matkustajista Participant-olioiden muodossa
        """

        participants = self._participant_repository.find_by_guide(guide)

        return list(participants)

    def get_participants_by_guide_and_travel(self, guide, travel):
        """Palauttaa matkanjohtajaan ja valittuun matkaan liittyvät matkustajat

        Args:
            guide: Merkkijono, joka kuvastaa matkustajan matkanjohtajaa
            travel: Mekkijono, joka kuvastaa matkustajan matkaa

        Returns:
            Lista kirjautuneeseen käyttäjään ja valittuun matkaan liittyvistä matkustajista
            Participant-olioiden muodossa
        """

        travels = self._participant_repository.find_by_guide_and_travel(
            guide, travel)

        return list(travels)

    def get_participants_by_name_and_guide(self, name, guide):
        """Palauttaa matkanjohtajaan ja valittuun matkaan liittyvät matkustajat

        Args:
            name: Merkkijono, joka kuvastaa matkustajan nimeä
            guide: Merkkijono, joka kuvastaa matkustajan matkanjohtajaa

        Returns:
            Lista kirjautuneeseen käyttäjään ja valittuun matkaan liittyvistä matkustajista
            Participant-olioiden muodossa
        """

        travels = self._participant_repository.find_by_name_and_guide(
            name, guide)

        return travels

    def get_all_participants(self):
        """Palauttaa kaikki matkustajat

        Returns:
            Lista matkoista Travel-olioiden muodossa
        """

        return self._participant_repository.find_all()


participant_service = ParticipantService()
