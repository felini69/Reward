from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Message'}),
        }
