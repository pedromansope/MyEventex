from django import forms
from django.core.exceptions import ValidationError


def validar_cpf(value):
    if not value.isdigit():
        raise ValidationError('Seu CPF deve conter apenas números', 'digitos')

    if len(value) != 11:
        raise ValidationError('CPF deve conter exatamente 11 números', 'tamanho')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validar_cpf])
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Telefone')