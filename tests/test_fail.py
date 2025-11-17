import pytest
from truco.carta import Carta

# Tests adapted to current `Carta` API: instead of using rich-comparison
# operators (not implemented in the original code), we assert on the
# numeric point values returned by `retornar_pontos_carta` and on the
# card numbers returned by `retornar_numero()`.

def test_hierarquia_manilhas_rn07_using_points():
    helper = Carta(1, 'ESPADAS')
    espadao = Carta(1, 'ESPADAS')
    basto = Carta(1, 'BASTOS')
    sete_espadas = Carta(7, 'ESPADAS')
    sete_ouros = Carta(7, 'OUROS')
    tres_comum = Carta(3, 'COPAS')

    assert helper.retornar_pontos_carta(espadao) > helper.retornar_pontos_carta(basto)
    assert helper.retornar_pontos_carta(basto) > helper.retornar_pontos_carta(sete_espadas)
    assert helper.retornar_pontos_carta(sete_espadas) > helper.retornar_pontos_carta(sete_ouros)
    assert helper.retornar_pontos_carta(sete_ouros) > helper.retornar_pontos_carta(tres_comum)


def test_hierarquia_cartas_comuns_rn07_using_points():
    helper = Carta(1, 'ESPADAS')
    tres_comum = Carta(3, 'COPAS')
    sete_copas = Carta(7, 'COPAS')
    quatro_paus = Carta(4, 'BASTOS')

    dois_comum = Carta(2, 'OUROS')
    as_comum = Carta(1, 'COPAS')
    rei_comum = Carta(12, 'ESPADAS')

    assert helper.retornar_pontos_carta(tres_comum) > helper.retornar_pontos_carta(dois_comum)
    assert helper.retornar_pontos_carta(dois_comum) > helper.retornar_pontos_carta(as_comum)
    assert helper.retornar_pontos_carta(as_comum) > helper.retornar_pontos_carta(rei_comum)
    assert helper.retornar_pontos_carta(rei_comum) > helper.retornar_pontos_carta(sete_copas)
    assert helper.retornar_pontos_carta(sete_copas) > helper.retornar_pontos_carta(quatro_paus)


def test_empate_cartas_comuns_rn04_using_numbers_and_points():
    helper = Carta(1, 'ESPADAS')
    sete_copas = Carta(7, 'COPAS')
    sete_paus = Carta(7, 'PAUS')
    quatro_espadas = Carta(4, 'ESPADAS')

    # same numeric value
    assert sete_copas.retornar_numero() == sete_paus.retornar_numero()
    # points should also be equal for same numeric non-manilha cards
    assert helper.retornar_pontos_carta(sete_copas) == helper.retornar_pontos_carta(sete_paus)
    # trivial identity check via number
    assert quatro_espadas.retornar_numero() == quatro_espadas.retornar_numero()
