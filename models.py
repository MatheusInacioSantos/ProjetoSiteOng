from django.db import models


# Create your models here.

class Cadastro(models.Model):
    situacao = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    nome = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300)
    local = models.CharField(max_length=150)
    info = models.CharField(max_length=150)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)

class Contato(models.Model):
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=14)
    descricao = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images/', max_length=100, default='images/profile/avatar-default-icon.png')

