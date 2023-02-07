from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    remember_me = forms.BooleanField(initial=True)

    def clean():
        # add custom errors
        if username is not None and password:
            return self.cleaned_data

