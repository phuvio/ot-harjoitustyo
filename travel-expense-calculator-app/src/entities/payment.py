class Payment:
    """Luokka, joka kuvaa yksittäistä maksutapahtumaa

    Attributes:
        travel: Merkkijono, joka kuvaa mihin matkaan maksutapahtuma liittyy
        receipt_name: Merkkijono, joka kuvaa maksutapahtuman nimeä
        date: Merkkijono, joka kuvaa maksutapahtuman päivämäärää
        amount: Numeroarvo, joka kuvaa maksutapahtuman summaa
        action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu
        payer: Merkkijono, joka kuvaa maksutapahtuman maksajaa
        information: Merkkijono, joka kuvaa maksutapahtuman lisätietoja
        payment_id: Merkkijono, joka kuvaa maksutapahtuman id:tä
    """

    def __init__(self, travel, receipt_name, date, amount, action,
                 payer, information, payment_id=None):
        """Luokan konstruktori, joka luo uuden maksutapahtuman

        Args:
            travel: Merkkijono, joka kuvaa mihin matkaan maksutapahtuma liittyy
            receipt_name: Merkkijono, joka kuvaa maksutapahtuman nimeä
            date: Merkkijono, joka kuvaa maksutapahtuman päivämäärää
            amount: Numeroarvo, joka kuvaa maksutapahtuman summaa
            action: Merkkijono, joka kuvaa onko maksutapahtuma ostos vai maksu
            payer: Merkkijono, joka kuvaa maksutapahtuman maksajaa
            information: Merkkijono, joka kuvaa maksutapahtuman lisätietoja
            payment_id: Merkkijono, joka kuvaa maksutapahtuman id:tä
        """

        self.travel = travel
        self.receipt_name = receipt_name
        self.date = date
        self.amount = amount
        self.action = action
        self.payer = payer
        self.information = information
        self.payment_id = payment_id
