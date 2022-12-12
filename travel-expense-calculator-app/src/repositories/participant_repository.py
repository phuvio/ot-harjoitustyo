from entities.participant import Patricipant
from database_connection import get_database_connection


def get_participant_by_row(row):
    return Patricipant(row["name"], row["travel"], row["guide"]) if row else None


class ParticipantRepository:
    """Matkustajiin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki matkustajat

        Returns:
            Palauttaa listan Participant-olioita
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM participants")

        rows = cursor.fetchall()

        return list(map(get_participant_by_row, rows))

    def find_by_guide(self, guide):
        """Palauttaa matkustajat matkanjohtajan käyttäjätunnuksen perusteella

        Args:
            guide: Matkanjohtajan käyttäjätunnus, johon liittyvät matkustajat palautetaan

        Returns:
            Palauttaa listan Participant-olioita, jos käyttäjätunnuksen omaavalla
            matkanjohtajalla on tallennettuja matkustajia
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM  participants WHERE guide = ?", (guide,))

        rows = cursor.fetchall()

        return list(map(get_participant_by_row, rows))

    def find_by_guide_and_travel(self, guide, travel):
        """Palauttaa matkustajat matkanjohtajan käyttäjätunnuksen ja valitun matkan perusteella

        Args:
            guide: Matkanjohtajan käyttäjätunnus, johon liittyvät matkustajat palautetaan
            travel: Matka, johon liittyvät matkustajat palautetaan

        Returns:
            Palauttaa listan Participant-olioita, jos käyttäjätunnuksen omaavalla matkanjohtajalla
            on tallennettuja matkustajia kyseiselle matkalle
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM participants WHERE travel = ? AND guide = ?", (travel, guide,))

        rows = cursor.fetchall()

        return list(map(get_participant_by_row, rows))

    def find_by_name_and_guide(self, name, guide):
        """Palauttaa matkustajan matkanjohtajan käyttäjätunnuksen ja valitun matkan perusteella

        Args:
            guide: Matkanjohtajan käyttäjätunnus, johon liittyvät matkustajat palautetaan
            travel: Matka, johon liittyvät matkustajat palautetaan

        Returns:
            Palauttaa Participant-olion, jos käyttäjätunnuksen omaavalla matkanjohtajalla
            on tallennettuja matkustaja kyseiselle matkalle
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM participants WHERE name = ? AND guide = ?", (name, guide,))

        row = cursor.fetchone()

        return get_participant_by_row(row)

    def create(self, participant):
        """Tallentaa matkustajan tietokantaan

        Args:
            participant: Tallennettava matkustaja Participant-oliona

        Returns:
            Tallennettu matkustaja Participant-oliona
        """

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO participants (name, travel, guide) VALUES (?,?,?)",
                       (participant.name, participant.travel, participant.guide))

        self._connection.commit()

        return participant

    def delete_all(self):
        """Poistaa kaikki matkustajat"""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM participants")

        self._connection.commit()


participant_repository = ParticipantRepository(get_database_connection())
