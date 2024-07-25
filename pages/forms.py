
from dataclasses import fields
from .models import ContactFormModel
from django import forms



class ContactFormModelForm(forms.ModelForm):
      class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'message']

        
    
