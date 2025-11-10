from pathlib import Path
import sys
import pytest
import inspect
import builtins

# Garante que o pacote SOURCE_TRUCO esteja importável durante os testes
ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "SOURCE_TRUCO"
sys.path.insert(0, str(SRC))

from truco.truco import Truco
from truco.carta import Carta
from truco.jogador import Jogador
from truco.flor import Flor
from truco.envido import Envido

def test_aumentoValorDeRodadaTruco(monkeypatch): #ERROR
    """Verifica se o valor da rodada aumenta corretamente após um pedido de Truco."""

    monkeypatch.setattr(builtins, 'input', lambda *a, **k: '1')
    
    j1 = Jogador('1')
    j2 = Jogador('2')
    t = Truco()
    t.estado_atual = ""

    t.controlador_truco(t, None, j1, j2, None)
    assert t.valor_aposta == 2

def test_aumentoValorDeRodadaRetruco(monkeypatch):
    """Verifica se o valor da rodada aumenta corretamente após um pedido de Retruco."""
    
    monkeypatch.setattr(builtins, 'input', lambda *a, **k: '1')
    
    j1 = Jogador('1')
    j2 = Jogador('2')
    t = Truco()
    t.estado_atual = "truco"

    t.controlador_truco(t, None, j1, j2, None)
    assert t.valor_aposta == 3

def test_aumentoValorDeRodadaVale4(monkeypatch):
    """Verifica se o valor da rodada aumenta corretamente após um pedido de Vale4."""
    
    monkeypatch.setattr(builtins, 'input', lambda *a, **k: '1')
    
    j1 = Jogador('1')
    j2 = Jogador('2')
    t = Truco()
    t.estado_atual = "retruco"

    t.controlador_truco(t, None, j1, j2, None)
    assert t.valor_aposta == 4

def test_ReconheceFlor(capsys):
    """Verifica se a opção de Flor é reconhecida quando está na mão do jogador."""

    j = Jogador("Test")
    f = Flor()
    j.mao = [Carta(1, 'ESPADAS'), Carta(2, 'ESPADAS'), Carta(3, 'ESPADAS')]
    j.flor = False

    assert j.checa_flor() == True

def test_PodeChamarFlorAposEnvido(capsys): #ERROR
    """Verifica se a opção de Flor é mostrada após uma chamada de Envido na rodada."""

    j = Jogador("Test")
    f = Flor()
    e = Envido()
    j.mao = [Carta(1, 'ESPADAS'), Carta(2, 'ESPADAS'), Carta(3, 'ESPADAS')]
    j.flor = False
    j.checa_flor()
    e.estado_atual = '6'
    
    j.mostrar_opcoes(None)
    captured = capsys.readouterr().out #read stdout & stderr, captured é apenas o .out (stdoutput, não stderror)

    assert 'Flor' not in captured


def test_SomaEnvido():
    """Verifica se o cálculo dos pontos do envido é feito corretamente"""

    j = Jogador('Test')
    j.mao = [Carta(6, 'ESPADAS'), Carta(2, 'OUROS'), Carta(4, 'ESPADAS')]
    
    result = j.calcula_envido(j.mao)

    assert result == 30

def test_SomaEnvidoComFlorNaMao(): #ERROR
    """Verifica se o cálculo dos pontos do envido é feito corretamente com uma Flor na mão"""

    j = Jogador('Test')
    j.mao = [Carta(10, 'ESPADAS'), Carta(3, 'ESPADAS'), Carta(12, 'ESPADAS')]
    
    result = j.calcula_envido(j.mao)

    assert result == 23