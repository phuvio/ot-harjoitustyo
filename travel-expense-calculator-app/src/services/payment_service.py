from entities.payment import Payment
from repositories.payment_repository import (
    payment_repository as default_payment_repository
)


class PaymentService:
    """Maksutapahtumiin liittyvästä sovelluslogiikasta vastaava luokka"""

    def __init__(self, payment_repository=default_payment_repository):
        """Luokan konstruktori. Luo uuden matkatapahtumiin liittyväst sovelluslogiikasta
        vastaavan luokan

        Args:
            payment_repository: Olio, jolla on PaymentRepository-luokkaa vastaavat metodit
        """

        self._payment = None
        self._payment_repository = payment_repository

    def create_payment(self, travel, receipt_name, date, amount,
                       action, payer, information):
        """Luo uuden maksutapahtuman

        Args:
            travel_id: Kokonaisluku, joka kuvaa matkan, johon maksutapahtuma liittyy, id:tä
            receipt_name: Merkkijono, joka kuvaa maksutapahtuman nimeä
            date: Merkkijono, joka kuvaa maksutapahtuman päivämäärää
            amount: Merkkijono, joka kuvaa maksutapahtuman summaa
            action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu
            payer: Merkkijono, joka kuvaa maksutapahtuman maksajaa
            information: Merkkijono, joka kuvaa maksutapahtuman lisätietoja

        Returns:
            Luotu maksutapahtuma Payment-olion muodossa
        """

        payment = Payment(travel, receipt_name, date, amount,
                          action, payer, information)

        return self._payment_repository.create(payment)

    def get_payments_by_travel_and_action(self, travel_id, action):
        """Palauttaa valittuun matkaan ja maksutapahtuman tyyppiin liittyvät maksutapahtumat

        Args:
            travel_id: Kokonaisluku, joka kuvaa mihin matkaan maksutapahtuma liittyy
            action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu

        Returns:
            Lista valittuun matkaan ja maksutapahtuman tyyppiin liittyvistä
            maksutapahtumista Payment-olioiden muodossa
        """

        payments = self._payment_repository.find_by_travel_and_transaction(
            travel_id,
            action
        )

        return list(payments)

    def get_payment_by_travel_and_name(self, travel_id, receipt_name):
        """Palauttaa valittuun matkaan ja maksun nimeen liittyvät maksutapahtumat

        Args:
            travel_id: Kokonaisluku, joka kuvaa mihin matkaan maksutapahtuma liittyy
            receipt_name: Merkkijono, joka kuvaa mihin maksuun maksutapahtuma liittyy

        Returns:
            Lista valittuun matkaan ja maksun nimeen liittyvistä
            maksutapahtumista Payment-olioiden muodossa
        """

        payments = self._payment_repository.find_by_travel_and_receipt_name(
            travel_id,
            receipt_name
        )

        return list(payments)

    def get_payment_by_travel_and_name_and_action(self, travel_id,
                                                  receipt_name, action):
        """Palauttaa valittuun matkaan ja maksun nimeen liittyvät maksutapahtumat

        Args:
            travel_id: Kokonaisluku, joka kuvaa mihin matkaan maksutapahtuma liittyy
            receipt_name: Merkkijono, joka kuvaa maksutapahtuman nimeä
            action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu

        Returns:
            Lista valittuun matkaan ja maksun nimeen liittyvistä
            maksutapahtumista Payment-olioiden muodossa
        """

        payments = self._payment_repository.find_by_travel_and_receipt_name_and_action(
            travel_id,
            receipt_name,
            action
        )

        return list(payments)

    def get_current_payment(self):
        """Palauttaa nykyisen maksun

        Returns:
            Palauttaa valitun maksun Payment-olion muodossa
        """

        return self._payment

    def get_all_payments(self):
        """Palauttaa kaikki maksutapahtumat

        Returns:
            Lista maksutapahtumista Payment-olioiden muodossa
        """

        return self._payment_repository.find_all()


payment_service = PaymentService()
