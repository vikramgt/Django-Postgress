from django import forms
from .models import Person


class CRUDFORM(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        
        "class": "form-control",
        "placeholder": "Last Name"
    }))
    
    class Meta:
        model = Person
        fields = [
            'first_name', 'last_name'
        ] 
