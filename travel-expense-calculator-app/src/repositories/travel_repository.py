from entities.travel import Travel


class TravelRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from travels")

        rows = cursor.fetchall()

        return [Travel(row["name"], row["guide"], row["participants"]) for row in rows]

    def create(self, travel):
        cursor = self._connection.cursor()
        
        sql = ''' INSERT INTO travels(name, guide, participants)
                  VALUES(?,?,?) '''
        
        cursor.execute(sql, travel)
        self._connection.commit()
        return cursor.lastrowid

    def delete_all(self):
        cursor = self._connection.cursot()

        sql = ''' DROP TABLE [IF EXISTS] travels
                  '''

        cursor.execute(sql)
        self._connection.commit()
        