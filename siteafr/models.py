from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    idade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )

