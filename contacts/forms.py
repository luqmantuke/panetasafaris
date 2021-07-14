from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ('full_name', 'email', 'subject', 'message')
        widget = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})

        }
