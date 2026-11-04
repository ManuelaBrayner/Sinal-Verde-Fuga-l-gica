import random

from constantes import (
    ACERTOS_POR_NIVEL, ACERTOS_POR_REDUCAO, ALTURA, ALTURA_CRUZ, DIST_MAX,
    ESPACO_CRUZ, GANHO_ACERTO, LIMITE_PARADA, PERDA_ERRO, PONTOS_BASE,
    PONTOS_POR_SEGUNDO, PRESSAO_PERGUNTA, QUESTOES_RECENTES, TEMPO_MIN,
    TEMPOS, VEL_PASSO, centro_faixa,
)
from estado import estado
from questoes import QUESTOES


# ---------------- Níveis e tempo ----------------
def nivel_atual():
    """Sobe de nível a cada ACERTOS_POR_NIVEL acertos (máximo 3)."""
    return min(3, 1 + estado.acertos // ACERTOS_POR_NIVEL)


def tempo_do_nivel():
    """Tempo para responder: diminui 1 s a cada ACERTOS_POR_REDUCAO acertos."""
    base = TEMPOS[nivel_atual()]
    return max(TEMPO_MIN, base - estado.acertos // ACERTOS_POR_REDUCAO)

