from django.contrib import messages
from django.shortcuts import render
from .forms import FaleConoscoForm

def index_home(request):
    return render(request, 'index.html')


def fale_conosco(request):
    form = FaleConoscoForm(request.POST or None)

    if (str(request.method) == 'POST'):
        if (form.is_valid()):
            '''
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f"\n-- MENSAGEM ENVIADA -- \nNome: {nome} \nE-mail: {email} \nAssunto: {assunto} \nMensagem: {mensagem} \n----------")
            '''

            messages.success(request, 'E-mail enviado com sucesso!')
            form = FaleConoscoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'faleconosco.html', context)


def produto(request):
    return render(request, 'produto.html')



