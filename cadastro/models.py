from datetime import date
from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(blank=False, max_length=16)
    senha = models.CharField(blank=True, max_length=16)
    nasc = models.DateField(blank=False, default=date.today)

    def __str__(self) -> str:
        return self.usuario