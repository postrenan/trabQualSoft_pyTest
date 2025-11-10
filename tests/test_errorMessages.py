from pathlib import Path
import sys
import pytest

# Garante que o pacote SOURCE_TRUCO esteja importável durante os testes
ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "SOURCE_TRUCO"
sys.path.insert(0, str(SRC))

from truco.baralho import Baralho
from truco.jogador import Jogador
from truco.jogo import Jogo


def test_retirarCartaDeBaralhoVazio():
    """Retirar carta de um baralho vazio deve levantar IndexError com mensagem esperada."""
    b = Baralho()
    b.resetar()

    with pytest.raises(IndexError) as exc:
        b.retirar_carta()
    # mensagem padrão do list.pop() em Python
    assert "pop from empty list" in str(exc.value)


def test_CalculaEnvidoComMaoInvalida():
    """calcula_envido() com mão com menos de duas cartas deve levantar ValueError."""
    j = Jogador("Test")
    j.criar_mao(Baralho()) # cria mão com 3 cartas
    j.mao.pop() # 2 cartas na mão (calcula_envido() ainda deve funcionar)
    j.mao.pop() # 1 carta (calcula_envido() deve falhar)
    with pytest.raises(ValueError) as exc:
        j.calcula_envido(j.mao)
    # mensagem típica do max() quando vazio
    assert "max() iterable argument is empty" in str(exc.value)