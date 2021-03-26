from django import forms
from .models import Contatos

class FormContatos(forms.ModelForm):
    Email = forms.EmailField(label='E-mail', required = True)
    class Meta:
        model = Contatos
        fields = ['Nome', 'Numero', 'Email']
