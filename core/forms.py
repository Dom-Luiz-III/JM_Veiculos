from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and not telefone.isdigit():
            raise forms.ValidationError("Por favor, insira um número de telefone válido.")
        return telefone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.islower():
            raise forms.ValidationError("Por favor, insira um endereço de e-mail válido em letras minúsculas.")
        return email