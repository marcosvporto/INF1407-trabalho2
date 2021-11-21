from django import forms 
from clientes.models import Pessoa, Plano, Consulta
from django.conf import settings
from django.contrib.admin import widgets
import datetime as dt
class ClienteModel2Form(forms.ModelForm): 
    dtNasc = forms.DateField( 
        label='Data de nascimento',
        widget=forms.SelectDateWidget(years=range(1980, dt.date.today().year-5)))
    
    def __init__(self, *args, **kwargs):
        super(ClienteModel2Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta: 
        model = Pessoa 
        fields = ['nome','CPF','email','telefone','dtNasc']


class ClienteUpdateModel2Form(forms.ModelForm):
    dtNasc = forms.DateField( 
        label='Data de nascimento',
        widget=forms.SelectDateWidget(years=range(1980, dt.date.today().year-5)))
    
    def __init__(self, *args, **kwargs):
        super(ClienteUpdateModel2Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta: 
        model = Pessoa 
        fields = ['nome','email','telefone','plano','dtNasc']
        
class PlanoModel2Form(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(PlanoModel2Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta: 
        model = Plano 
        fields = '__all__'


class ConsultaModel2Form(forms.ModelForm): 
    data = forms.DateField(
        label='Data',
        widget=forms.SelectDateWidget(years=range(dt.date.today().year,2023)))
    def __init__(self, *args, **kwargs):
        super(ConsultaModel2Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta: 
        model = Consulta 
        fields = ['especialidade','data','horario','pessoa','precoOriginal']



class ClienteConsultaForm(forms.Form):
    CPF = forms.IntegerField(min_value=00000000000,max_value=99999999999,help_text='Entre com seu CPF usando apenas números')
    
