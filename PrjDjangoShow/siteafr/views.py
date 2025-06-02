from django.shortcuts import render

def index(request):
    return render(request, 'siteafr/index.html')

def doacao(request):
    return render(request, 'siteafr/doacao.html')

def atendimento(request):
    return render(request, 'siteafr/atendimento.html')

def nossahistoria(request):
    return render(request, 'siteafr/nossahistoria.html')

def governanca(request):
    return render(request, 'siteafr/governanca.html')

def transparencia(request):
    return render(request, 'siteafr/transparencia.html')

def certificacoes(request):
    return render(request, 'siteafr/certificacoes.html')

def reabilitacao(request):
    return render(request, 'siteafr/reabilitação.html')

def sistema_restrito_afr(request):
    return render(request, 'siteafr/sistema-restrito-afr.html')

def cooperacao(request):
    return render(request, 'siteafr/cooperacao.html')

def sac(request):
    return render(request, 'siteafr/sac.html')

def visita(request):
    return render(request, 'siteafr/visita.html')

def trabalheconosco(request):
    return render(request, 'siteafr/trabalheconosco.html')

def voluntariado(request):
    return render(request, 'siteafr/voluntariado.html')

def unidadefluminense(request):
    return render(request, 'siteafr/unidadefluminense.html')

def unidadelisaura(request):
    return render(request, 'siteafr/unidadelisaura.html')


