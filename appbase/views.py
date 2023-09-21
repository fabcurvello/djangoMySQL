from django.shortcuts import render

def index_home(request):
    return render(request, 'index.html')


def fale_conosco(request):
    return render(request, 'faleconosco.html')


def produto(request):
    return render(request, 'produto.html')



