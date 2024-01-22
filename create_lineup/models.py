from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class Escalacoes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(null=False, max_length=200)
    img = models.ImageField(upload_to="static/img")
    def __str__(self):
        return self.titulo