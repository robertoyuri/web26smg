from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'crm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CRM'}),
            'uf_crm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidade'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }
        labels = {
            'nome': 'Nome',
            'crm': 'CRM',
            'uf_crm': 'UF',
            'especialidade': 'Especialidade',
            'telefone': 'Telefone',
            'email': 'E-mail',
        }

