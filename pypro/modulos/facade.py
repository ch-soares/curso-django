from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    '''
    Lista módulos ordenados por títulos
    '''

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def lista_aulas_de_modulos_ordenadas(modulo: Modulo):
    return modulo.aula_set.order_by('order').all()


def encontrar_aula(slug: str) -> Aula:
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
    ).all()
