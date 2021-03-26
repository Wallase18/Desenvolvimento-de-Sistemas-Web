from django.db import models

# Create your models here.
class manga(models.Model):
    nome = models.CharField(max_length = 200)
    Descricoa = models.TextField()
    imagem = models.ImageField(null=True, blank=True, upload_to='media')
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor = models.CharField(max_length = 200)
    # voto = models.IntegerField()
    comentario = models.TextField()
    def __str__(self):
        return self.autor
