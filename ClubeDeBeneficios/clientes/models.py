from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    CPF = models.CharField(max_length=11, primary_key=True,help_text='Entre com seu CPF usando apenas números')
    email = models.EmailField(help_text='Informe o email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',verbose_name='Data de nascimento')

class Plano(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre com o nome do Plano')
    qtConsulta = models.IntegerField(help_text='Consultas com desconto no mês')
    desconto = models.IntegerField(help_text='Percentual de Desconto nas Consultas')

class Cadastro(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    qtdConsultas = models.IntegerField(help_text='Percentual de Desconto nas Consultas')

class Consulta(models.Model):
    especialidade = models.CharField(max_length=100, help_text='Entre com a especialidade')
    horario = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',verbose_name='Data de nascimento')
    pessoa = models.OneToOneField(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)

def __str__(self):
    return self.nome