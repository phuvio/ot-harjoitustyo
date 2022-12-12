from entities.travel import Travel
from database_connection import get_database_connection


def get_travel_by_row(row):
    return Travel(row["name"], row["guide"], row["travel_id"]) if row else None


class TravelRepository:
    """Matkoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki matkat

        Returns:
            Palauttaa listan Travel-olioita
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM travels")

        rows = cursor.fetchall()

        return [Travel(row["name"], row["guide"], row["travel_id"]) for row in rows]

    def find_by_name(self, name):
        """Palauttaa matkat matkan nimen perusteella

        Args:
            name: Matkan nimi, johon liittyvät matkat palautetaan

        Returns:
            Palauttaa listan Travel-olioita, jos nimen omaavia
            matkoja on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM travels WHERE name = ?", (name,))

        row = cursor.fetchone()

        return get_travel_by_row(row)

    def find_by_guide(self, guide):
        """Palauttaa matkat matkan matkanjohtajan nimen perusteella

        Args:
            guide: Matkan matkanjohtajan nimi, johon liittyvät matkat palautetaan

        Returns:
            Palauttaa listan Travel-olioita, jos matkanjohtajan nimen omaavia
            matkoja on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM travels WHERE guide = ?", (guide,))

        rows = cursor.fetchall()

        return [Travel(row["name"], row["guide"], row["travel_id"]) for row in rows]

    def find_by_name_and_guide(self, name, guide):
        """Palauttaa matkan matkan nimen ja matkanjohtajan perusteella

        Args:
            name: Matkan nimi, johon liittyvä matka palautetaan
            guide: Matkan matkanjohtajan nimi, johon liittyvä matka palautetaan

        Returns:
            Palauttaa Travel-olion, jos matkan ja matkanjohtajan nimellä omaava
            matka on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM travels WHERE name = ? AND guide = ?", (name, guide,))

        row = cursor.fetchone()

        return get_travel_by_row(row)

    def create(self, travel):
        """Tallentaa matkan tietokantaan

        Args:
            travel: Tallennettava matka Travel-oliona

        Returns:
            Tallennettu matkustaja Travel-oliona
        """

        cursor = self._connection.cursor()

        sql = ''' INSERT INTO travels(name, guide)
                  VALUES(?,?) '''

        cursor.execute(sql, (travel.name, travel.guide))
        self._connection.commit()
        return cursor.lastrowid

    def delete_all(self):
        """Poistaa kaikki matkat
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM travels")

        self._connection.commit()


travel_repository = TravelRepository(get_database_connection())
