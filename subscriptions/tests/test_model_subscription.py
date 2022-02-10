from datetime import datetime
from django.test import TestCase
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Pedro Lucas',
            cpf='98745632451',
            email='pedrolucasmppe@gmail.com',
            phone='81-987445687'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription deve ter um auto created_at"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Pedro Lucas', str(self.obj))

    def test_paid_to_false(self):
        """por padrão o pagamento deve ser False"""
        self.assertEqual(False, self.obj.paid)
