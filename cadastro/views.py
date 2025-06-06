from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import PessoaForm


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # redireciona para uma página de sucesso
    else:
        form = PessoaForm()

        return render(request, 'cadastro/formulario.html', {'form': form})


def sucesso(request):
    return render(request, 'cadastro/sucesso.html')



def pagina_qualquer(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # ou outra página que quiser
    else:
        form = PessoaForm()

    return render(request, 'paginaqualquer.html', {'form': form})