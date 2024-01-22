from django import forms 
from .models import *

class FormacoesForm(forms.ModelForm):
    class Meta:
        model = Formacoes
        fields = ["nome", 'num_jogadores',
                  'p1x', 'p1y',
                  'p2x', 'p2y',
                  'p3x', 'p3y',
                  'p4x', 'p4y',
                  'p5x', 'p5y',
                  'p6x', 'p6y',
                  'p7x', 'p7y',
                  'p8x', 'p8y',
                  'p9x', 'p9y',

                  'p10x', 'p10y',
                  'p11x', 'p11y',
                  ]
    