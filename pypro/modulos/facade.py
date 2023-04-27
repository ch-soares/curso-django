from typing import List

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
    return Aula.objects.get(slug=slug)
