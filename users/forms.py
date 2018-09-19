
from django import forms

from .models import Email

class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['email']
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter an email',
                'aria-label': 'Email'}
            )
        }