from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    #Digito test
    def test_cpf_is_digit(self):
        """CPF DEVE CONTER APENAS DIGITOS"""
        form = self.form_valido(cpf='ABDE8798754')
        self.assertErroCod(form, 'cpf', 'digitos')

    def cpf_apenas_11digitos(self):
        "CPF deve conter apenas 11 digitos"
        form = self.form_valido(cpf='4785')
        self.assertErroCod(form, 'cpf', 'tamanho')

    def test_nome_captalized(self):
        #PEDRO lucas -> Pedro Lucas
        form = self.form_valido(name='PEDRO lucas')
        self.assertEqual('Pedro Lucas', form.cleaned_data['name'])

    def assertErroCod(self, form, field, code):
        errors = form.erros.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertMsgError(self, form, field, msg):
        errors = form.erros
        errors_list = errors[field]
        self.assertEqual([msg], errors_list)

    def form_valido(self, **kwargs):
        valido = dict(name='Pedro Lucas', cpf='12557874896',
                      email='pedrolucasmppe@gmail.com', phone='81-987445247')
        data = dict(valido, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

