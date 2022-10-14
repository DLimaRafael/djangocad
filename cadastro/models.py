from django.db import models

# Create your models here.
class User(models.Model):
    usuario = models.TextField(blank=False)
    senha = models.TextField(blank=True)
    nasc = models.DateField(blank=False)

    def __str__(self) -> str:
        return super().__str__()