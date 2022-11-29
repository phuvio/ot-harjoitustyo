from entities.travel import Travel
from database_connection import get_database_connection


def get_travel_by_row(row):
    return Travel(row["name"], row["participants"]) if row else None


class TravelRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM travels")

        rows = cursor.fetchall()

        return [Travel(row["name"], row["participants"]) for row in rows]

    def find_by_name(self, name):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM travels WHERE name = ?", (name,))

        row = cursor.fetchone()

        return get_travel_by_row(row)

    def find_by_participant(self, participant):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM travels WHERE participants = ?", (participant,))

        rows = cursor.fetchall()

        return [Travel(row["name"], row["participants"]) for row in rows]

    def create(self, travel):
        cursor = self._connection.cursor()

        sql = ''' INSERT INTO travels(name, participants)
                  VALUES(?,?) '''

        cursor.execute(sql, (travel.name, travel.participants))
        self._connection.commit()
        return cursor.lastrowid

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM travels")

        self._connection.commit()


travel_repository = TravelRepository(get_database_connection())
