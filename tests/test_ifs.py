from pathlib import Path
import sys
import pytest
import builtins

# garantir import do pacote SOURCE_TRUCO
ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "SOURCE_TRUCO"
sys.path.insert(0, str(SRC))

from truco.interface import Interface
from truco.carta import Carta
from truco.jogador import Jogador
from truco.truco import Truco
from truco.jogo import Jogo


def test_mostraTodasOpçoes(capsys):
    """Ao início da rodada, se o jogador tem 3 cartas e flor disponível, mostrar_opcoes lista Truco, Envido e Flor."""
    j = Jogador('P')
    t = Truco()
    j.mao = [Carta(1, 'ESPADAS'), Carta(2, 'ESPADAS'), Carta(3, 'ESPADAS')]
    j.pediu_truco = False
    t.estado_atual = ''
    j.flor = False
    assert j.checa_flor() == True

    j.mostrar_opcoes(None)
    captured = capsys.readouterr().out

    assert 'Truco' in captured
    assert 'Retruco' not in captured
    assert 'Envido' in captured
    assert 'Flor' in captured
    
def test_mostraOpçoesLimitadas(capsys): #ERROR
    """Se após truco ser chamado o jogador tem 3 cartas e não tem flor disponível, mostrar_opcoes deve listar apenas Retruco e Envidos."""
    j1 = Jogador('1')
    j2 = Jogador('2')
    t = Truco()
    j1.mao = [Carta(10, 'ESPADAS'), Carta(2, 'BASTOS'), Carta(6, 'OUROS')]
    j1.pediu_truco = True
    t.estado_atual = 'truco'
    t.jogador_bloqueado = j2
    t.controlador_truco(None, None, j2, j1, j2)
    j1.flor = False
    assert j1.checa_flor() == False
    j1.mostrar_opcoes(None)
    captured = capsys.readouterr().out

    assert 'Truco' not in captured
    assert 'Retruco' in captured
    assert 'Envido' in captured
    assert 'Flor' not in captured


def test_podePedirTruco2x(capsys):
    """Se jogador já pediu truco, opção Truco não deve aparecer (mesmo com 3 cartas)."""
    j = Jogador('P')
    j.mao = [Carta(1, 'ESPADAS'), Carta(2, 'OUROS'), Carta(3, 'COPAS')]
    j.pediu_truco = True

    j.mostrar_opcoes(None)
    out = capsys.readouterr().out

    assert 'Truco' not in out


def test_adicionarRodadaGanha():
    """Verifica se a adição de rodadas é contabilizada corretamente."""
    jogo = Jogo()
    interface = Interface()
    j1 = Jogador('1')
    j2 = Jogador('2')
    c1 = Carta(3, 'ESPADAS')
    c2 = Carta(2, 'OUROS')
    
    ganhador = jogo.verificar_ganhador(c1, c2, interface)
    assert jogo.adicionar_rodada(j1, j2, c1, c2, ganhador) == 1
    assert j1.rodadas == 1
    assert j2.rodadas == 0


def test_VerificaCartaVencedoraManilha():
    """Verifica se quando ambas as cartas jogadas são manilha, a vitória da rodada é contabilizada corretamente."""
    jogo = Jogo()

    c1 = Carta(1, 'ESPADAS')
    c2 = Carta(1, 'BASTOS')

    winner = jogo.verificar_carta_vencedora(c1, c2)
    assert winner is c1


def test_VerificaCartaVencedoraSemManilha():
    """Verifica se quando ambas as cartas são jogadas a vitória da rodada é contabilizada corretamente"""
    jogo = Jogo()

    c1 = Carta(3, 'COPAS')
    c2 = Carta(2, 'OUROS')

    winner = jogo.verificar_carta_vencedora(c1, c2)
    assert winner is c1

def test_VerificaCartaVencedoraMisturado():
    """Verifica se quando cartas com valores não-crescentes são jogadas a vitória da rodada é contabilizada corretamente"""
    jogo = Jogo()

    c1 = Carta(10, 'BASTOS')
    c2 = Carta(2, 'OUROS')

    winner = jogo.verificar_carta_vencedora(c1, c2)
    assert winner is c2