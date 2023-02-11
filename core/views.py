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


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm( request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


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

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm( request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)

def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


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


def movimentorotativo_update(request, id):
    data = {}
    movimentorotativo = MovimentoRotativo.objects.get(id=id)
    form = MovimentoRotativoForm( request.POST or None, instance=movimentorotativo)
    data['movimentorotativo'] = movimentorotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movimentosrotativos')
    else:
        return render(request, 'core/update_movimentorotativo.html', data)


def movimentorotativo_delete(request, id):
    movimentorotativo = MovimentoRotativo.objects.get(id=id)
    if request.method == 'POST':
        movimentorotativo.delete()
        return redirect('core_lista_movimentosrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movimentorotativo})


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


def movimentomensal_update(request, id):
    data = {}
    movimentomensal = MovimentoMensal.objects.get(id=id)
    form = MovimentoMensalForm( request.POST or None, instance=movimentomensal)
    data['movimentomensal'] = movimentomensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movimentosmensais')
    else:
        return render(request, 'core/update_movimentomensal.html', data)


def movimentomensal_delete(request, id):
    movimentomensal = MovimentoMensal.objects.get(id=id)
    if request.method == 'POST':
        movimentomensal.delete()
        return redirect('core_lista_movimentosmensais')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movimentomensal})


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


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm( request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


