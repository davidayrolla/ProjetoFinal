from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovimentoRotativo, MovimentoMensal, Mensalista
from .forms import PessoaForm, VeiculoForm, MovimentoRotativoForm, MovimentoMensalForm, MensalistaForm


def home(request):
    context={'mensagem': 'Olá,mundo'}
    return render(request, 'core/index.html', context )

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data =  {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data )


def pessoa_nova(request):
    form = PessoaForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html',data )


def veiculo_novo(request):
    form = VeiculoForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def lista_movimentosrotativos(request):
    movimentosrotativos = MovimentoRotativo.objects.all()
    form = MovimentoRotativoForm()
    data = {'movimentosrotativos': movimentosrotativos, 'form': form}
    return render(request, 'core/lista_movimentosrotativos.html', data )


def movimentorotativo_novo(request):
    form = MovimentoRotativoForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentosrotativos')


def lista_movimentosmensais(request):
    movimentosmensais = MovimentoMensal.objects.all()
    form = MovimentoMensalForm()
    data = {'movimentosmensais': movimentosmensais, 'form': form}
    return render(request, 'core/lista_movimentosmensais.html', data )


def movimentomensal_novo(request):
    form = MovimentoMensalForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentosmensais')

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data )

def mensalista_novo(request):
    form = MensalistaForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


