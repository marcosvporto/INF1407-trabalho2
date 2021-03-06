from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa, Plano, Consulta
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from clientes.forms import ClienteModel2Form, ClienteUpdateModel2Form
from clientes.forms import PlanoModel2Form
from clientes.forms import ConsultaModel2Form, ClienteConsultaForm
from django.http.response import HttpResponseRedirect 
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class ClientesListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        context = {'pessoas':pessoas, }
        return render(request, 'clientes/listaClientes.html', context)


class ClienteCreateView(View): 
    def get(self, request, *args, **kwargs): 
        context = { 'formulario': ClienteModel2Form, } 
        return render(request,"clientes/criaCliente.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = ClienteModel2Form(request.POST) 
        if formulario.is_valid(): 
            cliente = formulario.save() 
            cliente.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:verifica-cliente"))
        context = { 'formulario': ClienteModel2Form, } 
        return render(request,"clientes/criaCliente.html", context)
        
class ClienteUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ClienteUpdateModel2Form(instance=pessoa)
        context = {'formulario':formulario, }
        return render(request, 'clientes/atualizaCliente.html', context)
    
    def post(self, request, pk, *args, **kwargs): 
        pessoa = get_object_or_404(Pessoa, pk=pk) 
        formulario = ClienteUpdateModel2Form(request.POST, instance=pessoa)
        print("Plano", formulario['plano'].value()) 
        if formulario.is_valid(): 
            pessoa = formulario.save() 
            pessoa.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:lista-clientes")) 
        else: 
            context = {'pessoa': formulario, } 
            return render(request, 'clientes/atualizaCliente.html', context)


class ClienteDeleteView(View): 
    def get(self, request, pk, *args, **kwargs): 
        pessoa = Pessoa.objects.get(pk=pk) 
        context = {'pessoa': pessoa, } 
        return render( 
            request, 'clientes/apagaCliente.html',  
              context)  
    def post(self, request, pk, *args, **kwargs): 
        pessoa = Pessoa.objects.get(pk=pk) 
        pessoa.delete() 
        print("Removendo o cliente", pk) 
        return HttpResponseRedirect( 
            reverse_lazy("clientes:lista-clientes"))
    
class PlanosListView(View):
    def get(self, request, *args, **kwargs):
        planos = Plano.objects.all()
        context = {'planos':planos, }
        return render(request, 'clientes/listaPlanos.html', context)

class PlanoCreateView(View): 
    def get(self, request, *args, **kwargs): 
        context = { 'formulario': PlanoModel2Form, } 
        return render(request,"clientes/criaPlano.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = PlanoModel2Form(request.POST) 
        if formulario.is_valid(): 
            plano = formulario.save() 
            plano.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:lista-planos"))
        context = { 'formulario': PlanoModel2Form, } 
        return render(request,"clientes/criaPlano.html", context)


class PlanoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        plano = get_object_or_404(Plano, pk=pk)
        formulario = PlanoModel2Form(instance=plano)
        context = {'formulario':formulario, }
        return render(request, 'clientes/atualizaPlano.html', context)
    
    def post(self, request, pk, *args, **kwargs): 
        plano = get_object_or_404(Plano, pk=pk) 
        formulario = PlanoModel2Form(request.POST, instance=plano) 
        if formulario.is_valid(): 
            plano = formulario.save() 
            plano.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:lista-planos")) 
        else: 
            context = {'plano': formulario, } 
            return render(request, 'clientes/atualizaPlano.html', context)


class PlanoDeleteView(View): 
    def get(self, request, pk, *args, **kwargs): 
        plano = Plano.objects.get(pk=pk) 
        context = {'plano': plano, } 
        return render( 
            request, 'clientes/apagaPlano.html', context)  
    def post(self, request, pk, *args, **kwargs): 
        plano = Plano.objects.get(pk=pk) 
        plano.delete() 
        print("Removendo o plano", pk) 
        return HttpResponseRedirect( 
            reverse_lazy("clientes:lista-planos"))


#Consultas
class ConsultaListView(View):
    def get(self, request, *args, **kwargs):
        consultas = Consulta.objects.all()
        context = {'consultas':consultas, }
        return render(request, 'clientes/listaConsultas.html', context)

class ConsultaCreateView(View): 
    def get(self, request, *args, **kwargs): 
        context = { 'formulario': ConsultaModel2Form, } 
        return render(request,"clientes/criaConsulta.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = ConsultaModel2Form(request.POST) 
        
        if formulario.is_valid(): 
            consulta = formulario.save() 
            consulta.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas"))
        context = { 'formulario': ConsultaModel2Form, } 
        return render(request,"clientes/criaConsulta.html", context)


class ConsultaUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        consulta = get_object_or_404(Consulta, pk=pk)
        formulario = ConsultaModel2Form(instance=consulta)
        context = {'formulario':formulario, }
        return render(request, 'clientes/atualizaConsulta.html', context)

    def post(self, request, pk, *args, **kwargs): 
        consulta = get_object_or_404(Consulta, pk=pk) 
        formulario = ConsultaModel2Form(request.POST, instance=consulta)
        cpfPessoa = formulario['pessoa'].value()
        if cpfPessoa != "":  
            try:
                pessoa = Pessoa.objects.get(pk=cpfPessoa)
                if pessoa != None:
                    plano = pessoa.plano
                    if plano != None:
                        desconto = plano.desconto
                        if formulario.is_valid():
                            consulta = formulario.save()
                            valorSemDesconto =  formulario['precoOriginal'].value()
                            consulta.precoDesconto = ((100 - desconto) / 100) * float(valorSemDesconto) 
                            consulta.save()
                            return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas"))
                        else:
                            context = { 'formulario': ConsultaModel2Form, } 
                            return render(request,"clientes/criaConsulta.html", context)
                if formulario.is_valid():
                    consulta = formulario.save()
                    consulta.precoDesconto = consulta.precoOriginal 
                    consulta.save() 
                    return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas")) 
                else: 
                        context = {'pessoa': formulario, } 
                        return render(request, 'clientes/atualizaConsulta.html', context)
                    
            except ObjectDoesNotExist:
                context = { 'formulario': ConsultaModel2Form, } 
                return render(request,"clientes/criaConsulta.html", context)
        if formulario.is_valid():
            consulta = formulario.save() 
            consulta.save() 
            return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas")) 
        else: 
                context = {'pessoa': formulario, } 
                return render(request, 'clientes/atualizaConsulta.html', context)    
    
    # def post(self, request, pk, *args, **kwargs): 
    #     consulta = get_object_or_404(Consulta, pk=pk) 
    #     formulario = ConsultaModel2Form(request.POST, instance=consulta)
    #     cpfPessoa = formulario['pessoa'].value()
    #     try:
    #         pessoa = Pessoa.objects.get(pk=cpfPessoa)
    #         print('Pessoa:',pessoa)
    #         if Pessoa != None:
    #             print('--1---')
    #             plano = pessoa.plano
    #             if plano != None:
    #                 print('--2---')
    #                 desconto = pessoa.desconto
    #                 if formulario.is_valid(): 
    #                     print('--3---')
    #                     consulta = formulario.save()
    #                     valorSemDesconto =  formulario['precoOriginal'].value()
    #                     consulta.precoDesconto = ((100 - desconto) / 100) * float(valorSemDesconto) 
    #                     consulta.save()
    #                     return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas"))  
    #                     print('--4---')           
    #         if formulario.is_valid(): 
    #             print('--6---')
    #             consulta = formulario.save()
    #             consulta.save()
    #             return HttpResponseRedirect(reverse_lazy("clientes:lista-consultas")) 
    #         else:
    #             print('--7---')
    #             context = {'consulta': formulario, }
    #             return render(request, 'clientes/atualizaConsulta.html', context)
    #     except ObjectDoesNotExist:
    #         print('--8---')
    #         context = { 'formulario': ConsultaModel2Form, } 
    #         return render(request,"clientes/criaConsulta.html", context)
                

class ConsultaDeleteView(View): 
    def get(self, request, pk, *args, **kwargs): 
        consulta = Consulta.objects.get(pk=pk) 
        context = {'consulta': consulta, } 
        return render( 
            request, 'clientes/apagaConsulta.html', context)  
    def post(self, request, pk, *args, **kwargs): 
        consulta = Consulta.objects.get(pk=pk) 
        consulta.delete() 
        print("Removendo a consulta", pk) 
        return HttpResponseRedirect( 
            reverse_lazy("clientes:lista-consultas"))

class AgendaClienteView(CreateView):
    def get(self, request, *args, **kwargs): 
        context = { 'formulario': ClienteConsultaForm, } 
        return render(request,"clientes/verificaClienteAjax.html", context) 

class ClienteConsultaListView(View):
    def get(self, request, pk, *args, **kwargs):
        cliente = get_object_or_404(Pessoa, pk=pk)
        consultas = Consulta.objects.filter(pessoa = cliente)
        context = {'consultas':consultas, }
        return render(request, 'clientes/listaConsultasCliente.html', context)

def verificaCliente(request):
    cpf = request.GET.get("CPF", None)
    if Pessoa.objects.filter(CPF=cpf).exists():
        pessoa = Pessoa.objects.get(pk=cpf)
        consultas = Consulta.objects.filter(pessoa= pessoa)
        ser_consultas = serializers.serialize("json", consultas)
        return JsonResponse({"consultas":ser_consultas})
    return JsonResponse({"consultas":False})    

class PlanosConsultasListView(View):
    def get(self, request, *args, **kwargs):
        consultas = Consulta.objects.all()
        planos = Plano.objects.all()
        context = {'planos':planos, }
        print(context)
        return render(request, 'clientes/listaPlanos.html', context)