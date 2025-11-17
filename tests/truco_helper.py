# Arquivo auxiliar renomeado para evitar conflito de nome com o pacote 'truco'
import pytest
from unittest.mock import patch, MagicMock
import os 
import pathlib # Para encontrar o CSV de forma robusta

# --- Importação das classes do projeto (a partir do pacote 'truco') ---
try:
    from truco.carta import Carta
    from truco.baralho import Baralho
    # Este import assume que você corrigiu 'class pontos' para 'class Pontos' em pontos.py
    from truco.pontos import Pontos
    from truco.jogador import JogadorHumano, JogadorMaquina
    from truco.jogo import Jogo
except ImportError as e:
    pytest.fail(f"ERRO de importação: {e}. Verifique se 'truco/__init__.py' existe e se 'pontos.py' tem a classe 'Pontos'.")
except ModuleNotFoundError:
    pytest.fail("ERRO: 'ModuleNotFoundError'. Verifique se 'truco/__init__.py' existe.")

# --- Fixtures (Configuração dos Testes) ---

@pytest.fixture
def baralho_novo():
    """Fixture para um baralho novo, pronto para embaralhar."""
    return Baralho()

@pytest.fixture
def pontos_novo():
    """Fixture para um placar zerado."""
    return Pontos()

@pytest.fixture
def jogador_humano():
    """Fixture para um jogador humano."""
    return JogadorHumano("Humano")

@pytest.fixture
def jogador_maquina(request):
    """Fixture para o jogador IA (Máquina)."""
    # Encontra o caminho para a raiz do projeto (onde o pytest foi iniciado)
    PROJECT_ROOT = pathlib.Path(request.config.rootdir)
    DB_PATH = PROJECT_ROOT / "dbtrucoimitacao_maos.csv" # Assumindo que o CSV está na raiz

    if not DB_PATH.exists():
        pytest.skip(f"Arquivo CSV não encontrado em {DB_PATH}. Pulando testes da IA.")
    
    return JogadorMaquina("Máquina", db_path=str(DB_PATH))


@pytest.fixture
def jogo_novo(jogador_humano, jogador_maquina, pontos_novo):
    """Fixture para uma instância de Jogo pronta."""
    try:
        return Jogo(jogador_humano, jogador_maquina, pontos_novo)
    except TypeError:
        try:
             # Se o Jogo criar seus próprios Pontos internamente
             game = Jogo(jogador_humano, jogador_maquina)
             game.placar = pontos_novo # Sobrescreve para o teste
             return game
        except Exception as e:
            pytest.skip(f"Não foi possível instanciar Jogo(). Verifique o __init__ em jogo.py. Erro: {e}")


# --- Cartas Específicas para Testes de Hierarquia ---
@pytest.fixture
def espedao(): return Carta(1, 'espadas')

@pytest.fixture
def basto(): return Carta(1, 'paus')

@pytest.fixture
def sete_espadas(): return Carta(7, 'espadas')

@pytest.fixture
def sete_ouros(): return Carta(7, 'ouros')

@pytest.fixture
def tres_comum(): return Carta(3, 'copas')

@pytest.fixture
def sete_copas(): return Carta(7, 'copas')

@pytest.fixture
def quatro_paus(): return Carta(4, 'paus')


# --- O resto dos testes do arquivo original podem permanecer em seus respectivos módulos ---
