import random
import pytest
from truco.carta import Carta
from truco.baralho import Baralho


def test_retornar_carta_e_naipe():
    c = Carta(4, 'ESPADAS')
    assert c.retornar_carta() == '4 de ESPADAS'
    assert c.retornar_numero() == 4
    assert c.retornar_naipe() == 'ESPADAS'


def test_retorna_naipe_codificado():
    mapping = {'ESPADAS': 1, 'OUROS': 2, 'BASTOS': 3, 'COPAS': 4}
    for name, code in mapping.items():
        assert Carta(1, name).retornar_naipe_codificado() == code


def test_retornar_pontos_envido():
    c = Carta(7, 'COPAS')
    assert c.retornar_pontos_envido(c) == 7


def test_verificar_carta_alta_baixa_e_retornar_pontos():
    c3 = Carta(3, 'ESPADAS')
    c2 = Carta(2, 'COPAS')
    helper = Carta(1, 'ESPADAS')
    assert helper.verificar_carta_alta(c3, c2) is c3
    assert helper.verificar_carta_baixa(c3, c2) is c2


def test_classificar_carta():
    a = Carta(3, 'ESPADAS')
    b = Carta(2, 'COPAS')
    c = Carta(4, 'BASTOS')
    helper = Carta(1, 'ESPADAS')
    pontos, classes = helper.classificar_carta([a, b, c])
    assert len(pontos) == 3
    assert 'Alta' in classes
    assert 'Baixa' in classes
    assert 'Media' in classes


def test_baralho_criar_retirar_tamanho():
    bar = Baralho()
    assert len(bar.cartas) == 40
    card = bar.retirar_carta()
    assert isinstance(card, Carta)
    assert len(bar.cartas) == 39


def test_embaralhar_troca_ordem():
    bar = Baralho()
    original = list(bar.cartas)
    random.seed(0)
    bar.embaralhar()
    assert bar.cartas != original


def test_retirar_from_empty_raises():
    bar = Baralho()
    bar.resetar()
    with pytest.raises(IndexError):
        bar.retirar_carta()



def test_hierarquia_manilhas_usando_pontos():
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


def test_hierarquia_cartas_comuns_usando_pontos():
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


def test_empate_cartas_comuns_numeros_pontos():
    helper = Carta(1, 'ESPADAS')
    sete_copas = Carta(7, 'COPAS')
    sete_paus = Carta(7, 'PAUS')
    quatro_espadas = Carta(4, 'ESPADAS')

    assert sete_copas.retornar_numero() == sete_paus.retornar_numero()
    assert helper.retornar_pontos_carta(sete_copas) == helper.retornar_pontos_carta(sete_paus)
    assert quatro_espadas.retornar_numero() == quatro_espadas.retornar_numero()
