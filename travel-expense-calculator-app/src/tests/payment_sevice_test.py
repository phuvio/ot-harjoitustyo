import unittest
from entities.payment import Payment
from services.payment_service import PaymentService
from repositories.payment_repository import payment_repository


class FakePaymentRepository:
    def __init__(self, payments=None):
        self.payments = payments or []

    def find_all(self):
        return self.payments

    def find_by_travel_and_action(self, travel, action):
        matching_payments = filter(
            lambda payment: payment.travel == travel and payment.action == action,
            self.payments
        )

        matching_payments_list = list(matching_payments)

        return matching_payments_list

    def create(self, payment):
        self.payments.append(payment)

        return payment


class TestPaymentService(unittest.TestCase):
    def setUp(self):
        self.payment_service = PaymentService(
            payment_repository
        )
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
        self._buy_22 = Payment(
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
        travel = "Toka matka"
        receipt_name = "Kuitti"
        date = "10.10."
        amount = "300"
        action = "maksu"
        payer = "Jaana"
        information = "Tarina"
        id = "8"

        self.payment_service.create_payment(
            travel,
            receipt_name,
            date,
            amount,
            action,
            payer,
            information,
            id
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
            "Eka matka", "maksu")

        self.assertEqual(len(payments), 2)
        self.assertEqual(payments[0].receipt_name, self._pay_1.receipt_name)
        self.assertEqual(payments[1].receipt_name, self._pay_2.receipt_name)
