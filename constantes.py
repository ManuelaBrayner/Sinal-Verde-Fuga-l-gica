# ---- Janela ----
LARGURA, ALTURA = 800, 600
FPS = 60
TITULO = 'Sinal Verde: Fuga Lógica'

# ---- Pista (3 faixas entre as calçadas) ----
PISTA_X0, PISTA_X1 = 150, 650
N_FAIXAS = 3
LARGURA_FAIXA = (PISTA_X1 - PISTA_X0) / N_FAIXAS

# ---- Carros ----
CARRO_L, CARRO_A = 54, 94          # largura e altura de cada carro
CARRO_Y = 270                      # posição vertical fixa do carro de fuga
ESCALA_DIST = 0.5                  # converte "distância lógica" em pixels na tela

# ---- Cruzamentos ----
ALTURA_CRUZ = 110                  # altura da rua transversal
ESPACO_CRUZ = 600                  # pixels rolados entre um cruzamento e outro
LIMITE_PARADA = CARRO_Y - 20       # onde a borda de baixo do cruzamento para

# ---- Velocidade da pista (pixels por segundo) ----
VEL_INICIAL = 240
VEL_PASSO = 10                     # aumento a cada cruzamento aberto

# ---- Distância entre a viatura e o carro de fuga ----
DIST_INICIAL = 240
DIST_MAX = 400                     # a viatura nunca fica mais longe que isso
GANHO_ACERTO = 100                 # quanto a viatura se afasta ao acertar
PERDA_ERRO = 120                   # quanto a viatura se aproxima ao errar
PRESSAO_PERGUNTA = 0               # px/s que a viatura avança durante a pergunta (0 = desligado)

# ---- Tempo para responder (segundos) ----
TEMPOS = {1: 15, 2: 12, 3: 10}     # tempo base por nível
TEMPO_MIN = 6                      # o tempo nunca fica menor que isso
ACERTOS_POR_REDUCAO = 3            # a cada N acertos, o tempo cai 1 s

# ---- Níveis e pontuação ----
ACERTOS_POR_NIVEL = 4              # a cada N acertos, sobe de nível (até o 3)
PONTOS_BASE = 100
PONTOS_POR_SEGUNDO = 10            # bônus por segundo restante

# ---- Questões ----
QUESTOES_RECENTES = 3              # não repete as últimas N questões

# ---- Cores (R, G, B) ----
COR_ASFALTO = (43, 46, 54)
COR_CALCADA = (61, 65, 80)
COR_RUA = (53, 57, 68)
COR_FAIXA = (230, 230, 230)
COR_TEXTO = (241, 243, 247)
COR_TEXTO_SUAVE = (170, 176, 191)
COR_DESTAQUE = (255, 90, 31)
COR_VERDE = (46, 204, 113)
COR_VERMELHO = (231, 76, 60)
COR_AMARELO = (241, 196, 15)
COR_PAINEL = (29, 32, 41)
COR_FUNDO = (18, 20, 26)


def centro_faixa(indice):
    """Devolve a posição X do centro da faixa (0, 1 ou 2)."""
    return PISTA_X0 + LARGURA_FAIXA * (indice + 0.5)

