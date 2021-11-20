from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa
from django.views.generic.base import View
from clientes.forms import ClienteModel2Form, ClienteUpdateModel2Form
from clientes.forms import PlanoModel2Form
from django.http.response import HttpResponseRedirect 
from django.urls.base import reverse_lazy
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
            return HttpResponseRedirect(reverse_lazy("clientes:lista-clientes"))
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
        formulario = ClienteModel2Form(request.POST, instance=pessoa) 
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