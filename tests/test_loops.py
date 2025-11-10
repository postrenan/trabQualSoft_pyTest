from pathlib import Path
import sys
import pytest

# Garante que o pacote SOURCE_TRUCO esteja importável durante os testes
ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "SOURCE_TRUCO"
sys.path.insert(0, str(SRC))

from truco.baralho import Baralho
from truco.jogo import Jogo

def test_loopCriacaoBaralho():
    """Reseta o baralho e verifica se criar_baralho() está criando o baralho corretamente."""
    b = Baralho()
    b.resetar()
    b.criar_baralho()

    assert len(b.cartas) == 40
    primeira = b.cartas[0]
    ultima = b.cartas[-1]
    assert primeira.retornar_numero() == 1
    assert primeira.retornar_naipe() == "ESPADAS"
    assert ultima.retornar_numero() == 12
    assert ultima.retornar_naipe() == "BASTOS"

def test_loopCriacaoMaoJogadores3Cartas():
    """Verifica que criar_mao() para jogador e bot itera 3 vezes (3 cartas por mão)."""
    baralho = Baralho()
    jogo = Jogo()
    jogador = jogo.criar_jogador("Alice", baralho)
    bot = jogo.criar_bot("Bot", baralho)
    assert len(jogador.mao) == 3
    assert len(bot.mao) == 3
    # 6 cartas retiradas do baralho
    assert len(baralho.cartas) == 40 - 6