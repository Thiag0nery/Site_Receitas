from django import forms
from django.contrib.auth.models import User

class UserForms(forms.ModelForm):
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
    class Meta:
        model = User
        fields = ('username','password','email','password2')