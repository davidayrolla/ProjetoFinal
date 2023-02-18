from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pessoa, Veiculo, MovimentoRotativo, MovimentoMensal, Mensalista
from .forms import PessoaForm, VeiculoForm, MovimentoRotativoForm, MovimentoMensalForm, MensalistaForm
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
import csv



def home(request):
    return render(request, 'core/index.html' )


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data =  {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data )


@login_required
def pessoa_nova(request):
    form = PessoaForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
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


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html',data )


@login_required
def veiculo_novo(request):
    form = VeiculoForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
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


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


@login_required
def lista_movimentosrotativos(request):
    movimentosrotativos = MovimentoRotativo.objects.all()
    form = MovimentoRotativoForm()
    data = {'movimentosrotativos': movimentosrotativos, 'form': form}
    return render(request, 'core/lista_movimentosrotativos.html', data )


@login_required
def movimentorotativo_novo(request):
    form = MovimentoRotativoForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentosrotativos')


@login_required
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


@login_required
def movimentorotativo_delete(request, id):
    movimentorotativo = MovimentoRotativo.objects.get(id=id)
    if request.method == 'POST':
        movimentorotativo.delete()
        return redirect('core_lista_movimentosrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movimentorotativo})


@login_required
def lista_movimentosmensais(request):
    movimentosmensais = MovimentoMensal.objects.all()
    form = MovimentoMensalForm()
    data = {'movimentosmensais': movimentosmensais, 'form': form}
    return render(request, 'core/lista_movimentosmensais.html', data )


@login_required
def movimentomensal_novo(request):
    form = MovimentoMensalForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_movimentosmensais')


@login_required
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


@login_required
def movimentomensal_delete(request, id):
    movimentomensal = MovimentoMensal.objects.get(id=id)
    if request.method == 'POST':
        movimentomensal.delete()
        return redirect('core_lista_movimentosmensais')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movimentomensal})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data )


@login_required
def mensalista_novo(request):
    form = MensalistaForm( request.POST or None )
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
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


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render( 'core/relatorio.html', params, 'relatorios_veiculos')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response

