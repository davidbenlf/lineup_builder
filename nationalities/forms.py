from django import forms 
from .models import *

class NacionalidadesForm(forms.ModelForm):
    class Meta:
        model = Nacionalidades
        fields = ["img", "nome"]
    