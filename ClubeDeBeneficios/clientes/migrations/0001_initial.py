# Generated by Django 3.2.8 on 2021-11-20 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('nome', models.CharField(help_text='Entre o nome', max_length=100)),
                ('CPF', models.CharField(help_text='Entre com seu CPF usando apenas números', max_length=11, primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='Informe o email', max_length=254)),
                ('telefone', models.CharField(help_text='Telefone com DDD e DDI', max_length=20)),
                ('dtNasc', models.DateField(help_text='Nascimento no formato DD/MM/AAAA', verbose_name='Data de nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre com o nome do Plano', max_length=100)),
                ('qtConsulta', models.IntegerField(help_text='Consultas com desconto no mês')),
                ('desconto', models.IntegerField(help_text='Percentual de Desconto nas Consultas')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(help_text='Entre com a especialidade', max_length=100)),
                ('horario', models.DateField(help_text='Nascimento no formato DD/MM/AAAA', verbose_name='Data de nascimento')),
                ('pessoa', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtdConsultas', models.IntegerField(help_text='Percentual de Desconto nas Consultas')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.pessoa')),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.plano')),
            ],
        ),
    ]
