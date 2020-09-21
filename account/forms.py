from django import forms


class LoginForm(forms.Form):
    """ форма для авторизации на сайте """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
