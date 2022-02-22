from unittest.mock import Mock

from django.test import TestCase
from subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Pedro Lucas', cpf='12354785985',
                                    email='pedrolucasmppe@gmail.com', phone='81997445878')

        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Marcar como pago"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """deve marcar todas as subscrisções como pagas"""
        self.call_action()
        #verifica o resultado se tem efeito colateral, chamando a action

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """deve enviar uma mensagem de confirmação ao usuário"""
        mock = self.call_action()

        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_action(self):
        queryset = Subscription.objects.all()
        # chamar a action

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock