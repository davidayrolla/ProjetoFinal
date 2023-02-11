from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200,blank=True,null=True)
    telefone = models.CharField(max_length=20,blank=True,null=True)

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

