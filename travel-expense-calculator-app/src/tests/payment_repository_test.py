import unittest
from repositories.payment_repository import payment_repository
from entities.payment import Payment


class TestPaymentRepository(unittest.TestCase):
    def setUp(self):
        payment_repository.delete_all()

        self._pay_1 = Payment(
            1,
            "hotelli",
            "23.11.",
            "200",
            "maksu",
            "Jaana",
            "Plaza Milano -hotelli"
        )
        self._buy_11 = Payment(
            1,
            "hotelli",
            "23.11.",
            "100",
            "ostos",
            "Jaana",
            "Plaza Milano -hotelli"
        )
        self._buy_12 = Payment(
            1,
            "hotelli",
            "23.11.",
            "100",
            "ostos",
            "p",
            "Plaza Milano -hotelli"
        )
        self._pay_2 = Payment(
            2,
            "juna",
            "24.11.",
            "150",
            "maksu",
            "p",
            "juna Milano-Torino"
        )
        self._buy_21 = Payment(
            2,
            "juna",
            "24.11.",
            "50",
            "ostos",
            "Jaana",
            "juna Milano-Torino"
        )
        self._buy_22 = Payment(
            2,
            "juna",
            "24.11.",
            "50",
            "ostos",
            "p",
            "juna Milano-Torino"
        )
        self._buy_23 = Payment(
            2,
            "juna",
            "24.11.",
            "50",
            "ostos",
            "Mari",
            "juna Milano-Torino"
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

        self.assertEqual(len(buyings), 2)
        self.assertEqual(buyings[0].payer, self._buy_11.payer)
        self.assertEqual(buyings[1].payer, self._buy_22.payer)

        payings = payment_repository.find_by_travel_and_transaction(
            self._pay_1.travel,
            self._pay_1.action
        )
        self.assertEqual(len(payings), 1)
        self.assertEqual(payings[0].payer, self._buy_11.payer)

    def test_find_by_travel_and_receipt_name(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)
        payment_repository.create(self._buy_23)

        buyings = payment_repository.find_by_travel_and_receipt_name(
            self._pay_1.travel,
            self._pay_1.receipt_name
        )

        self.assertEqual(len(buyings), 3)
        self.assertEqual(buyings[0].amount, self._pay_1.amount)
        self.assertEqual(buyings[2].amount, self._buy_12.amount)

    def test_find_by_travel_and_receipt_name_and_action(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)
        payment_repository.create(self._buy_23)

        buyings = payment_repository.find_by_travel_and_receipt_name_and_action(
            self._pay_1.travel,
            self._pay_1.receipt_name,
            "maksu"
        )

        self.assertEqual(len(buyings), 1)
        self.assertEqual(buyings[0].payer, self._pay_1.payer)

    def tearDown(self):
        payment_repository.delete_all()
