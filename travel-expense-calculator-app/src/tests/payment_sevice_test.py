import unittest
from entities.payment import Payment
from services.payment_service import PaymentService
from repositories.payment_repository import payment_repository


class TestPaymentService(unittest.TestCase):
    def setUp(self):
        self.payment_service = PaymentService(
            payment_repository
        )
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
        self._buy_22 = Payment(
            2,
            "juna",
            "24.11.",
            "50",
            "ostos",
            "Mari",
            "juna Milano-Torino"
        )

    def test_create_payment(self):
        travel = 2
        receipt_name = "Kuitti"
        date = "10.10."
        amount = "300"
        action = "maksu"
        payer = "Jaana"
        information = "Tarina"

        self.payment_service.create_payment(
            travel,
            receipt_name,
            date,
            amount,
            action,
            payer,
            information
        )
        payments = self.payment_service.get_all_payments()

        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].receipt_name, receipt_name)

    def test_get_payments_by_travel_and_action(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)

        payments = self.payment_service.get_payments_by_travel_and_action(
            1, "maksu")

        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].receipt_name, self._pay_1.receipt_name)

    def test_get_payments_by_travel_and_receipt_name(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)

        payments = self.payment_service.get_payment_by_travel_and_name(
            self._pay_1.travel,
            self._pay_1.receipt_name
        )

        self.assertEqual(len(payments), 3)
        self.assertEqual(payments[0].receipt_name, self._pay_1.receipt_name)
        self.assertEqual(payments[2].information, self._buy_12.information)

    def test_get_payments_by_travel_and_name_and_action(self):
        payment_repository.create(self._pay_1)
        payment_repository.create(self._buy_11)
        payment_repository.create(self._buy_12)
        payment_repository.create(self._pay_2)
        payment_repository.create(self._buy_21)
        payment_repository.create(self._buy_22)

        payments = self.payment_service.get_payment_by_travel_and_name_and_action(
            self._pay_1.travel,
            self._pay_1.receipt_name,
            "maksu"
        )

        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].receipt_name, self._pay_1.receipt_name)

    def tearDown(self):
        payment_repository.delete_all()
