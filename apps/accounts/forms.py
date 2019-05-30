from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

    # -> Validation
    character_field_message = "Apenas letras são aceitas."

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name.replace(' ', '').isalpha():
            raise forms.ValidationError(self.character_field_message)

        return first_name

    def clean_last_name(self):

        last_name = self.cleaned_data.get('last_name')

        if not last_name.replace(' ', '').isalpha():
            raise forms.ValidationError(self.character_field_message)

        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username.replace(' ', '').isalpha():
            raise forms.ValidationError(self.character_field_message)

        username_exists = User.objects.filter(username=username)
        if username_exists:
            raise forms.ValidationError("Este nome de usuário já existe.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_exists = User.objects.filter(email=email)
        if email_exists:
            raise forms.ValidationError("Este email já existe.")

        return email
