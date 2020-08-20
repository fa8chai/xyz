from django.contrib.auth.forms import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    passing_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Profile
        fields= ('school','passing_date',)