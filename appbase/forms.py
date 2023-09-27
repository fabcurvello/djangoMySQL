from django import forms
from django.core.mail import EmailMessage


class FaleConoscoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=80)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=150)
    mensagem = forms.CharField(label='Mensagem', max_length=255, widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f"Nome: {nome} \nE-mail \nAssunto: {assunto} \nMensagem: {mensagem}"

        mail = EmailMessage(
            subject="E-mail enviado pelo sistema DjangoMySQL",
            body=conteudo,
            from_email="faleconosco@seudominio.com.br",
            to=["contato@seudominio.com.br", "outro@seudominio.com.br"],
            headers={"Reply-To": email}
        )
        mail.send()









