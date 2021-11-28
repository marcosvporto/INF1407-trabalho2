from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.views.generic.base import View
from clientes.models import Pessoa, Plano, Consulta

class MeuUpdateView(UpdateView): 
  def get(self, request, pk, *args, **kwargs): 
    if request.user.id == pk: 
      return super().get(request, pk, args, kwargs) 
    else: 
      return redirect('sec-paginaProfile')

def homePage(request):
  return render(request,'ClubeDeBeneficios/index.html')
  
def homeSec(request):
    return render(request, "registro/paginaProfile.html")

def registro(request): 
    if request.method == 'POST': 
        formulario = UserCreationForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save() 
            return redirect('sec-login') 
        
    else: 
        formulario = UserCreationForm() 
    context = {'formulario': formulario, } 
    return render( request, 'registro/registro.html', context)

def paginaProfile(request):
    return render(request, 'registro/paginaProfile.html')

class PlanosConsultasListView(View):
    def get(self, request, *args, **kwargs):
        consultas = Consulta.objects.filter(pessoa= None)
        planos = Plano.objects.all()
        context = {'planos':planos, 'consultas':consultas }
        return render(request, 'ClubeDeBeneficios/index.html', context)