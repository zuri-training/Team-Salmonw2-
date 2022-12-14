from django import forms
from .models import Donation, Donate


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'school', 'reason', 'card_number', 'bank_name', 'amount']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
