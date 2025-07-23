from django import forms
from .models import MenuItem


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # redirect = cleaned_data.get('redirect')
        # page = cleaned_data.get('page')

        # if not redirect and not page:
        #     raise forms.ValidationError("Enter redirect URL, or page.")
        
        return cleaned_data

