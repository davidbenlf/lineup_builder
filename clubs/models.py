from django.db import models

# Create your models here.
class Times(models.Model):
    img = models.ImageField(upload_to="static/img")
    nome = models.CharField(null=False, unique=True, max_length=200)
    def __str__(self):
        return self.nome