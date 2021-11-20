from django import forms 
from clientes.models import Pessoa, Plano 
from django.conf import settings

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