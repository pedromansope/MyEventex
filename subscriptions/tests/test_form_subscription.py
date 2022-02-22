from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_fields(self):
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    #Digito test
    def test_cpf_is_digit(self):
        """CPF DEVE CONTER APENAS DIGITOS"""
        data = dict(name='Pedro Lucas', cpf='ABCD5678921',
                    email='pedrolucasmppe@gmail.com', phone='81-987445321')
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertListEqual(['cpf', list(form.errors)])

    def cpf_apenas_11digitos(self):
        "CPF deve conter apenas 11 digitos"
        data = dict(name='Pedro Lucas', cpf='7821',
                    email='pedrolucasmppe@gmail.com', phone='81-987445321')
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertListEqual(['cpf'], list(form.errors))


