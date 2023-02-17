from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^$', home, name='core_home'),

    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoanova/$', pessoa_nova, name='core_pessoa_nova'),
    re_path(r'^pessoaupdate/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoadelete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculonovo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculoupdate/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculodelete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),

    re_path(r'^movimentosrotativos/$', lista_movimentosrotativos, name='core_lista_movimentosrotativos'),
    re_path(r'^movimentorotativonovo/$', movimentorotativo_novo, name='core_movimentorotativo_novo'),
    re_path(r'^movimentorotativoupdate/(?P<id>\d+)/$', movimentorotativo_update, name='core_movimentorotativo_update'),
    re_path(r'^movimentorotativodelete/(?P<id>\d+)/$', movimentorotativo_delete, name='core_movimentorotativo_delete'),

    re_path(r'^movimentosmensais/$', lista_movimentosmensais, name='core_lista_movimentosmensais'),
    re_path(r'^movimentomensalnovo/$', movimentomensal_novo, name='core_movimentomensal_novo'),
    re_path(r'^movimentomensalupdate/(?P<id>\d+)/$', movimentomensal_update, name='core_movimentomensal_update'),
    re_path(r'^movimentomensaldelete/(?P<id>\d+)/$', movimentomensal_delete, name='core_movimentomensal_delete'),

    re_path(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^mensalistanovo/$', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalistaupdate/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalistadelete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),

]
