from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Post


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

    # First Name Validation
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        error_message = "Apenas letras são aceitas."

        if first_name.replace(' ', '').isalpha():
            return first_name
        else:
            raise forms.ValidationError(error_message)

    # Last Name Validation
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        error_message = "Apenas letras são aceitas."

        if last_name.replace(' ', '').isalpha():
            return last_name
        else:
            raise forms.ValidationError(error_message)

    # Username Validation
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Should be char
        error_message = "Apenas letras são aceitas."

        if username.replace(' ', '').isalpha():
            return username
        else:
            raise forms.ValidationError(error_message)

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


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'date')
