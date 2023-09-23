from django.shortcuts import render
from .forms import FaleConoscoForm

def index_home(request):
    return render(request, 'index.html')


def fale_conosco(request):
    form = FaleConoscoForm()
    context = {
        'form': form
    }
    return render(request, 'faleconosco.html', context)


def produto(request):
    return render(request, 'produto.html')



