# Generated by Django 3.2.8 on 2021-11-28 03:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre com o nome do Plano', max_length=100)),
                ('desconto', models.IntegerField(help_text='Percentual de Desconto nas Consultas')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome', models.CharField(help_text='Entre o nome', max_length=100)),
                ('CPF', models.CharField(help_text='Entre com seu CPF usando apenas números', max_length=11, primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='Informe o email', max_length=254)),
                ('telefone', models.CharField(help_text='Telefone com DDD e DDI', max_length=20)),
                ('dtNasc', models.DateField(help_text='Nascimento no formato DD/MM/AAAA', verbose_name='Data de nascimento')),
                ('plano', models.ForeignKey(blank=True, help_text='Selecione o Plano', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.plano')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(choices=[('NUTRI', 'Nutrição'), ('PSI', 'Psicologia'), ('ENDOCRINO', 'Endocrinologia'), ('GASTRO', 'Gastroentereologia'), ('OTORRINO', 'Otorrinolaringologia')], help_text='Entre com a especialidade', max_length=20)),
                ('precoOriginal', models.IntegerField(help_text='Preço Inicial da Consulta', verbose_name='Valor s/ Desconto')),
                ('precoDesconto', models.IntegerField(default=0, help_text='Valor a Ser Cobrado pela Consulta', verbose_name='Valor c/ Desconto')),
                ('data', models.DateField(help_text='Data da Consuta no formato DD/MM/AAAA', verbose_name='Data')),
                ('horario', models.TimeField(choices=[(datetime.time(7, 0), '07:00'), (datetime.time(9, 0), '09:00'), (datetime.time(11, 0), '11:00'), (datetime.time(13, 0), '13:00'), (datetime.time(15, 0), '15:00')], help_text='Hora da Consuta', verbose_name='Horário')),
                ('pessoa', models.ForeignKey(blank=True, help_text='Selecione o Paciente', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.pessoa')),
            ],
        ),
    ]
