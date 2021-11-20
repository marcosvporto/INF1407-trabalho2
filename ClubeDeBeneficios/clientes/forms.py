from django import forms 
from clientes.models import Pessoa, Plano, Consulta
from django.conf import settings
from django.contrib.admin import widgets
import datetime as dt
class ClienteModel2Form(forms.ModelForm): 
    dtNasc = forms.DateField( 
        input_formats=settings.DATE_INPUT_FORMATS,  
        label='Data de nascimento',
        help_text='Nascimento no formato DD/MM/AAAA')
    class Meta: 
        model = Pessoa 
        fields = ['nome','CPF','email','telefone','dtNasc']


class ClienteUpdateModel2Form(forms.ModelForm): 
    class Meta: 
        model = Pessoa 
        fields = ['nome','email','telefone','plano']
        plano = forms.ModelMultipleChoiceField(queryset=Plano.objects.all(), to_field_name='nome',widget=forms.Select())
        
class PlanoModel2Form(forms.ModelForm): 
    class Meta: 
        model = Plano 
        fields = '__all__'


class ConsultaModel2Form(forms.ModelForm): 
    data = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,  
        label='Data',
        help_text='Data da Consuta no formato DD/MM/AAAA',
        widget=widgets.AdminDateWidget())
    class Meta: 
        model = Consulta 
        fields = ['especialidade','data','horario','pessoa']
        
        
