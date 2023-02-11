from django.contrib import admin
from .models import *

class MovimentoRotativoAdmin(admin.ModelAdmin):
    list_display=('checkin', 'checkout', 'veiculo', 'valor_hora', 'horas_total', 'total', 'pago')

class MovimentoMensalAdmin(admin.ModelAdmin):
    list_display=('mensalista', 'dt_pgto', 'total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(MovimentoRotativo, MovimentoRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovimentoMensal, MovimentoMensalAdmin)