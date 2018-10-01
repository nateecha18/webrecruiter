from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Username',
            'autocomplete' : 'off',
        }
    ))
    first_name = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Your First Name',
            'autocomplete' : 'off',
            'style' : 'margin-top:25px;',
        }
    ))
    last_name = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Your Last Name',
            'autocomplete' : 'off',
            'style' : 'margin-top:25px;',
        }
    ))
    email = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter Email',
            'autocomplete' : 'off',
            'style' : 'margin-top:25px;',
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
    confirm_password=forms.CharField(label='',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Password Confirmation',
            'autocomplete' : 'off',
        }
    ))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match"
            )
