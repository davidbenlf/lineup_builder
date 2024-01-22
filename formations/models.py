from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class Formacoes(models.Model):
    num_jogadores = models.IntegerField(null=False, default=11, choices=((i,i) for i in range(1, 12)))
    nome = models.CharField(null=False, max_length=200)
    def __str__(self):
        return self.nome

    p1x = models.IntegerField(null=False)
    p1y = models.IntegerField(null=False)

    p2x = models.IntegerField(null=False)
    p2y = models.IntegerField(null=False)

    p3x = models.IntegerField(null=False)
    p3y = models.IntegerField(null=False)

    p4x = models.IntegerField(null=False)
    p4y = models.IntegerField(null=False)

    p5x = models.IntegerField(null=False)
    p5y = models.IntegerField(null=False)

    p6x = models.IntegerField(null=False)
    p6y = models.IntegerField(null=False)

    p7x = models.IntegerField(null=False)
    p7y = models.IntegerField(null=False)

    p8x = models.IntegerField(null=False)
    p8y = models.IntegerField(null=False)

    p9x = models.IntegerField(null=False)
    p9y = models.IntegerField(null=False)

    p10x = models.IntegerField(null=False)
    p10y = models.IntegerField(null=False)

    p11x = models.IntegerField(null=False)
    p11y = models.IntegerField(null=False)