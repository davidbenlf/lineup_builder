from django.db import models

# Create your models here. 
class Nacionalidades(models.Model):
    nome = models.CharField(null=False, max_length=200)
    img = models.ImageField(upload_to="static/img")
    def __str__(self):
        return self.nome