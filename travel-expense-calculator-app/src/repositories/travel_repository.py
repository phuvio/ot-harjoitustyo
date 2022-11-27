from entities.travel import Travel


class TravelRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM travels")

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

        sql = ''' DROP TABLE [IF EXISTS] travels
                  '''

        cursor.execute(sql)
        self._connection.commit()
