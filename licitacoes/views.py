from django.shortcuts import render
from .models import Licitacao

# Create your views here.
def lista_licitacoes(request):
    licitacoes = Licitacao.objects.all()
    return render(request, 'licitacoes/lista.html', {'licitacoes': licitacoes})