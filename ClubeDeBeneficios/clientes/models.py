from django.db import models
import datetime as dt
# Create your models here.

class Plano(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre com o nome do Plano')
    qtConsulta = models.IntegerField(help_text='Quantidade de consultas com desconto no mês', verbose_name='Consultas')
    desconto = models.IntegerField(help_text='Percentual de Desconto nas Consultas')
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    CPF = models.CharField(max_length=11, primary_key=True,help_text='Entre com seu CPF usando apenas números')
    email = models.EmailField(help_text='Informe o email', max_length=254)
    telefone = models.CharField(help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',verbose_name='Data de nascimento')
    plano = models.ManyToManyField(Plano)

    def __str__(self):
        return str(self.nome)+" - "+str(self.CPF)

class Consulta(models.Model):
    ESPECIALIDADES = (
        ("NUTRI", "Nutrição"),
        ("PSI", "Psicologia"),
        ("ENDOCRINO", "Endocrinologia"),
        ("GASTRO","Gastroentereologia"),
        ("OTORRINO","Otorrinolaringologia"),
    )
    HORARIOS = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(7, 17,2)]
    especialidade = models.CharField(max_length=20,choices=ESPECIALIDADES, help_text='Entre com a especialidade')
    data = models.DateField(help_text='Data da Consuta no formato DD/MM/AAAA',verbose_name='Data')
    horario = models.TimeField(help_text='Hora da Consuta',choices=HORARIOS,verbose_name='Horário')
    pessoa = models.OneToOneField(Pessoa, null=True, blank=True, on_delete=models.SET_NULL)
