from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
        authenticate,
        login,
        get_user_model,
        login,
        logout,
        )

user = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Username',
            'autocomplete' : 'off',
        }
    ))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-group form-control',
            'placeholder' : 'Password',
            'autocomplete' : 'off',
            'style' : 'margin-top:25px;',
        }
    ))


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username , password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)
