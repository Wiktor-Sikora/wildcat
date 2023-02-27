from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from django import forms

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    remember_me = forms.BooleanField(initial=True, required=False)

    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            return self.cleaned_data
        # add custom errors

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email'] # + fields from password1, password2, username

    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
