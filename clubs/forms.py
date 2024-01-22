from django import forms 
from .models import *

class TimesForm(forms.ModelForm):
    class Meta:
        model = Times
        fields = ["img", "nome"]
    