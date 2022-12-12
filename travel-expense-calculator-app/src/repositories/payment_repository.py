from entities.payment import Payment
from database_connection import get_database_connection


class PaymentRepository:
    """Maksutapahtumiin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki maksutapahtumat

        Returns:
            Palauttaa listan Payment-olioita
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM payments")

        rows = cursor.fetchall()

        return [Payment(
            row["travel"],
            row["receipt_name"],
            row["date"],
            row["amount"],
            row["action"],
            row["payer"],
            row["information"]) for row in rows]

    def find_by_travel_and_transaction(self, travel, action):
        """Palauttaa maksutapahtumat matkan nimen ja tapahtuman mukaan

        Args:
            travel: Matkan id, johon palautettavat maksutapahtumat liittyvät
            action: Tapahtuma, joka on joko ostos tai maksu

        Returns:
            Palauttaa listan Payment-olioita, jos matkan nimeen liittyviä
            maksutapahtumia on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM payments WHERE travel = ? AND action = ?", (travel, action))

        rows = cursor.fetchall()

        return [Payment(
            row["travel"],
            row["receipt_name"],
            row["date"],
            row["amount"],
            row["action"],
            row["payer"],
            row["information"]) for row in rows]

    def find_by_travel_and_receipt_name(self, travel, receipt_name):
        """Palauttaa maksutapahtumat matkan ja maksun nimien mukaan

        Args:
            travel: Matkan id, johon palautettavat maksutapahtumat liittyvät
            receipt_name: Maksun nimi, johon palautettavat maksutapahtumat liittyvät

        Returns:
            Palauttaa listan Payment-olioita, jos matkan nimeen liittyviä
            maksutapahtumia on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM payments WHERE travel = ? AND receipt_name = ?", (travel, receipt_name))

        rows = cursor.fetchall()

        return [Payment(
            row["travel"],
            row["receipt_name"],
            row["date"],
            row["amount"],
            row["action"],
            row["payer"],
            row["information"]) for row in rows]

    def find_by_travel_and_receipt_name_and_action(self, travel, receipt_name, action):
        """Palauttaa maksutapahtumat matkan ja maksun nimien mukaan

        Args:
            travel: Matkan id, johon palautettavat maksutapahtumat liittyvät
            receipt_name: Maksun nimi, johon palautettavat maksutapahtumat liittyvät
            action: Maksutapahtuman luonne, joko ostos tai maksu, johon maksutapahtumat liittyvät

        Returns:
            Palauttaa listan Payment-olioita, jos matkan nimeen liittyviä
            maksutapahtumia on tallennettu
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM payments WHERE travel = ? AND receipt_name = ? AND action = ?",
            (travel, receipt_name, action)
        )

        rows = cursor.fetchall()

        return [Payment(
            row["travel"],
            row["receipt_name"],
            row["date"],
            row["amount"],
            row["action"],
            row["payer"],
            row["information"]) for row in rows]

    def create(self, payment):
        """Tallentaa maksutapahtuman tietokantaan

        Args:
            payment: Tallennettava maksutapahtuma Payment-oliona
        Returns:
            Tallennettu maksutapahtuma Payment-oiliona
        """

        cursor = self._connection.cursor()

        sql = ''' INSERT INTO payments(travel,
                                       receipt_name, 
                                       date, 
                                       amount, 
                                       action, 
                                       payer, 
                                       information
                                       ) VALUES(?,?,?,?,?,?,?) '''

        cursor.execute(sql, (payment.travel,
                             payment.receipt_name,
                             payment.date,
                             payment.amount,
                             payment.action,
                             payment.payer,
                             payment.information)
                       )
        self._connection.commit()
        return cursor.lastrowid

    def delete_all(self):
        """Poistaa kaikki matkat
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM payments")

        self._connection.commit()


payment_repository = PaymentRepository(get_database_connection())
