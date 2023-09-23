from django import forms


class FaleConoscoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=80)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=150)
    mensagem = forms.CharField(label='Mensagem', max_length=255, widget=forms.Textarea())
