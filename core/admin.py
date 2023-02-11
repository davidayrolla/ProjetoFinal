from django.contrib import admin
from .models import *

class MovRotativoAdmin(admin.ModelAdmin):
    list_display=('checkin', 'checkout', 'veiculo', 'valor_hora', 'horas_total', 'total', 'pago')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(MovimentoRotativo, MovRotativoAdmin)
