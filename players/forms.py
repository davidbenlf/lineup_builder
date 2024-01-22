from django import forms 
from .models import *

class JogadoresForm(forms.ModelForm):
    class Meta:
        model = Jogadores
        fields = ["img", "nome", "nacionalidade", "time"]
    
    