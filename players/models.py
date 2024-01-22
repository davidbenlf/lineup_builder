from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

from nationalities.models import Nacionalidades
from clubs.models import Times

# Create your models here.

# class Times(models.Model):
#     nome = models.CharField(null=False, max_length=200)
#     img = models.ImageField(upload_to="static/img")
#     def __str__(self):
#         return self.nome
    
# class Nacionalidades(models.Model):
#     nome = models.CharField(null=False, max_length=200)
#     img = models.ImageField(upload_to="static/img")
#     def __str__(self):
#         return self.nome

class Jogadores(models.Model):
    nome = models.CharField(null=False, max_length=200)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)
    nacionalidade = models.ForeignKey(Nacionalidades, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="static/img")
    def __str__(self):
        return self.nome
    
    #pegar a nacionalidade/time do jogador sem precisar de outro request do cliente
    def get_nacionalidade(self):
        full_nacionalidade = {'nome': self.nacionalidade.nome, 'img': self.nacionalidade.img}
        return full_nacionalidade
    
    def get_time(self):
        full_time = {'nome': self.time.nome, 'img': self.time.img}
        return full_time
    
class NumJogadores(models.Model):
    value = models.IntegerField(null=False, default=11, validators=[MaxValueValidator(11), MinValueValidator(1)])