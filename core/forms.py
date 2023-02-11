from .models import Pessoa, Veiculo, MovimentoRotativo, MovimentoMensal, Mensalista
from django.forms import ModelForm

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovimentoRotativoForm(ModelForm):
    class Meta:
        model = MovimentoRotativo
        fields = '__all__'


class MovimentoMensalForm(ModelForm):
    class Meta:
        model = MovimentoMensal
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


