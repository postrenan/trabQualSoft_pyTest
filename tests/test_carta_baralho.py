import random
import pytest
from truco.carta import Carta
from truco.baralho import Baralho


def test_retornar_carta_and_accessors():
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


def test_verificar_carta_alta_baixa_and_retornar_pontos():
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


def test_baralho_criar_and_retirar_and_size():
    bar = Baralho()
    assert len(bar.cartas) == 40
    card = bar.retirar_carta()
    assert isinstance(card, Carta)
    assert len(bar.cartas) == 39


def test_embaralhar_changes_order():
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
