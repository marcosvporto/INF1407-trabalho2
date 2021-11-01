from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    email = models.EmailField(help_text='Informe o email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',verbose_name='Data de nascimento')

def __str__(self):
    return self.nome