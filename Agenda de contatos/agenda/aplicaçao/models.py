from django.db import models

# Create your models here.
class Contatos(models.Model):
    Nome = models.CharField(max_length=50)
    Numero = models.CharField(max_length=12)
    Email = models.CharField(max_length=50)
    def __str__(self):
        return self.Nome
