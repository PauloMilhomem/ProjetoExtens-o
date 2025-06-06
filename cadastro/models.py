from django.db import models

# Create your models here.

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)  # campo texto com tamanho máximo 100
    email = models.EmailField()  # campo para e-mail (validação automática)
    idade = models.IntegerField()  # campo inteiro

    def __str__(self):
        return self.nome  # para exibir o nome da pessoa em representações do objeto
