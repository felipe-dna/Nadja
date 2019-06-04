from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

    # Verifica se o
    def validate_character_field(self, field_value):
        error_message = "Apenas letras são aceitas."

        if field_value.replace(' ', '').isalpha():
            return field_value
        else:
            raise forms.ValidationError(error_message)

    # First Name Validation
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        self.validate_character_field(first_name)

    # Last Name Validation
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        self.validate_character_field(last_name)

    # Username Validation
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Should be char
        self.validate_character_field(username)

        # Should be unique
        username_exists = User.objects.filter(username=username)
        if username_exists:
            raise forms.ValidationError("Este nome de usuário já existe.")

        return username

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Should be unique
        email_exists = User.objects.filter(email=email)
        if email_exists:
            raise forms.ValidationError("Este email já existe.")

        return email
