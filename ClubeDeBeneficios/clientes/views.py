from django.shortcuts import render
from clientes.models import Pessoa
from django.views.generic.base import View

# Create your views here.
class ClientesListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        context = {'pessoas':pessoas, }
        return render(request, 'clientes/listaClientes.html', context)