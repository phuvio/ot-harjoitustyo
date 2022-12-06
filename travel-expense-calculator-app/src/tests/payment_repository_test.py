import unittest
from repositories.payment_repository import payment_repository
from entities.payment import Payment


class TestPaymentRepository(unittest.TestCase):
    def setUp(self):
        payment_repository.delete_all()

        self._pay_1 = Payment(
            "Eka matka",
            "hotelli",
            "23.11.",
            "200",
            "maksu",
            "Jaana",
            "Plaza Milano -hotelli",
            "1"
        )
        self._buy_11 = Payment(
            "Eka matka",
            "hotelli",
            "23.11.",
            "100",
            "ostos",
            "Jaana",
            "Plaza Milano -hotelli",
            "2"
        )
        self._buy_12 = Payment(
            "Eka matka",
            "hotelli",
            "23.11.",
            "100",
            "ostos",
            "p",
            "Plaza Milano -hotelli",
            "3"
        )
        self._pay_2 = Payment(
            "Eka matka",
            "juna",
            "24.11.",
            "150",
            "maksu",
            "p",
            "juna Milano-Torino",
            "4"
        )
        self._buy_21 = Payment(
            "Eka matka",
            "juna",
            "24.11.",
            "50",
            "ostos",
            "Jaana",
            "juna Milano-Torino",
            "5"
        )
        self._buy_22 = Payment(
            "Eka matka",
            "juna",
            "24.11.",
            "50",
            "ostos",
            "p",
            "juna Milano-Torino",
            "6"
        )
        self._buy_23 = Payment(
            "Eka matka",
            "juna",
            "24.11.",
            "50",
            "ostos",
            "Mari",
            "juna Milano-Torino",
            "7"
        )

    def test_create_payment(self):
        payment_repository.create(self._pay_1)
        payments = payment_repository.find_all()

        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].receipt_name, self._pay_1.receipt_name)

    def test_find_by_travel_and_transaction(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)
        payment_repository.create(self._buy_23)

        buyings = payment_repository.find_by_travel_and_transaction(
            self._pay_1.travel,
            self._buy_11.action
        )

        self.assertEqual(len(buyings), 5)
        self.assertEqual(buyings[0].payer, self._buy_11.payer)
        self.assertEqual(buyings[3].payer, self._buy_22.payer)

        payings = payment_repository.find_by_travel_and_transaction(
            self._pay_1.travel,
            self._pay_1.action
        )
        self.assertEqual(len(payings), 2)
        self.assertEqual(payings[0].payer, self._buy_11.payer)
