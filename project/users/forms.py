from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('name', 'email', 'phone', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': True,'placeholder':('Full Name'),'class':('name')})
        self.fields['email'].widget.attrs.update({'placeholder':('Email'),'class':('email')})
        self.fields['phone'].widget.attrs.update({'placeholder':('Phone Number'),'class':('phone')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password'),'class':('password1')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password'),'class':('password2')})

class LoginForm(forms.Form):
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'placeholder':('Phone Number'),'class':('phone')})
        self.fields['password'].widget.attrs.update({'placeholder':('password'),'class':('password')})


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('phone',)