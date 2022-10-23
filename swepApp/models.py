from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Alimentos(models.Model):
    nome = models.CharField(max_length=50)
    valorNutri = models.CharField(max_length=50)

class UserSwep(AbstractUser):
    pass

class Despensa(models.Model):
    alimentos = models.ManyToManyField(Alimentos)

class RegularUser(UserSwep):
    despensa = models.OneToOneField(Despensa, on_delete=models.CASCADE, null=True)

class Nutritionist(UserSwep):
    crn = models.CharField(max_length=50)

class Recipe(models.Model):
    titulo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=500)
    modoPreparo = models.TextField()
    author = models.ForeignKey(UserSwep, on_delete=models.CASCADE)
    Norte = 'NO'
    Nordeste = 'NE'
    CentroOeste = 'CO'
    Sul = 'SU'
    Sudeste = 'SE'
    regiaoEnum = [
        (Norte, 'Norte'),
        (Nordeste, 'Nordeste'),
        (CentroOeste, 'Centro-Oeste'),
        (Sul, 'Sul'),
        (Sudeste, 'Sudeste'),
    ]
    regiao = models.CharField(
        max_length=2,
        choices= regiaoEnum, 
        null=True)

    def str(self):
        return self.titulo

class Indicacoes(models.Model):
    description2 = models.TextField()
    tipo = models.CharField(max_length=50)
    author = models.ForeignKey(UserSwep, on_delete=models.CASCADE)

    def str(self):
        return self.decription2
