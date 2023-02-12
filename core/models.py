from django.db import models
import math


class Parametro(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parâmetros gerais'


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200,blank=True,null=True)
    telefone = models.CharField(max_length=20,blank=True,null=True)
    # documento = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.ForeignKey(Marca,blank=True,null=True, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    cor = models.CharField(max_length=15, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.placa + ' (' + self.marca.nome + ' - ' + self.proprietario.nome + ')'



class MovimentoRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        if self.checkout:
            return math.ceil( ( self.checkout - self.checkin ).total_seconds() / 3600 )
        else:
            return 0


    def total(self):
        return self.valor_hora * self.horas_total()


    def __str__(self):
        return f'{self.veiculo.placa} - {self.checkin}'

    class Meta:
        verbose_name_plural = 'movimentos rotativos'

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    fim = models.DateField(auto_now=False, null=True, blank=True)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.veiculo.placa} - {self.veiculo.proprietario.nome}'


class MovimentoMensal(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.mensalista} - {self.dt_pgto}'

    class Meta:
        verbose_name_plural = 'movimentos mensais'