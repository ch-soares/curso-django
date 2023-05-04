from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.lista_aulas_de_modulos_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})


def indice(request):
    contexto = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', contexto)
