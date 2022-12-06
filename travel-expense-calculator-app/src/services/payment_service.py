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
                       action, payer, information, payment_id=None):
        """Luo uuden maksutapahtuman

        Args:
            travel: Merkkijono, joka kuvaa mihin matkaan maksutapahtuma liittyy
            receipt_name: Merkkijono, joka kuvaa maksutapahtuman nimeä
            date: Merkkijono, joka kuvaa maksutapahtuman päivämäärää
            amount: Numeroarvo, joka kuvaa maksutapahtuman summaa
            action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu
            payer: Merkkijono, joka kuvaa maksutapahtuman maksajaa
            information: Merkkijono, joka kuvaa maksutapahtuman lisätietoja
            id: Merkkijono, joka kuvaa maksutapahtuman id:tä

        Returns:
            Luotu maksutapahtuma Payment-olion muodossa
        """

        payment = Payment(travel, receipt_name, date, amount,
                          action, payer, information, payment_id)

        return self._payment_repository.create(payment)

    def get_payments_by_travel_and_action(self, travel, action):
        """Palauttaa valittuun matkaan ja maksutapahtuman tyyppiin liittyvät maksutapahtumat

        Returns:
            Lista valittuun matkaan ja maksutapahtuman tyyppiin liittyvistä
            maksutapahtumista Payment-olioiden muodossa
        """

        payments = self._payment_repository.find_by_travel_and_transaction(
            travel,
            action
        )

        return list(payments)

    def get_all_payments(self):
        """Palauttaa kaikki maksutapahtumat

        Returns:
            Lista maksutapahtumista Payment-olioiden muodossa
        """

        return self._payment_repository.find_all()


payment_service = PaymentService()
