import pygame
import random

pygame.init()

largura = 450
altura = 500

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

linhas = 20
colunas = 10
tamanho_celula = 25

rodando = True
game_over = False
pontuacao = 0

intervalo_queda = 500
tempo_ultima_queda = pygame.time.get_ticks()


# -------------------------
# PEÇAS
# -------------------------

peca_i = [[1, 1, 1, 1]]

peca_o = [
    [1, 1],
    [1, 1],
]

peca_t = [
    [0, 1, 0],
    [1, 1, 1],
]

peca_l = [
    [1, 0],
    [1, 0],
    [1, 1],
]

peca_j = [
    [0, 1],
    [0, 1],
    [1, 1],
]

peca_s = [
    [0, 1, 1],
    [1, 1, 0],
]

peca_z = [
    [1, 1, 0],
    [0, 1, 1],
]

pecas = [
    peca_i,
    peca_o,
    peca_t,
    peca_l,
    peca_j,
    peca_s,
    peca_z,
]


# -------------------------
# CLASSE PECA
# -------------------------

class Peca:
    def __init__(self, formato):
        self.formato = formato
        self.linha = 0
        self.coluna = (colunas - len(formato[0])) // 2

    def rotacionar(self):
        return [
            list(linha)
            for linha in zip(*self.formato[::-1])
        ]

    def mover_esquerda(self):
        self.coluna -= 1

    def mover_direita(self):
        self.coluna += 1

    def descer(self):
        self.linha += 1
# -------------------------
# CRIAÇÃO DO TABULEIRO
# -------------------------

def criar_tabuleiro():
    novo_tabuleiro = []

    for linha in range(linhas):
        nova_linha = []

        for coluna in range(colunas):
            nova_linha.append(0)

        novo_tabuleiro.append(nova_linha)

    return novo_tabuleiro


tabuleiro = criar_tabuleiro()

peca_atual = Peca(random.choice(pecas))


# -------------------------
# DESENHO
# -------------------------

def desenhar_tabuleiro():
    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula

            if tabuleiro[linha][coluna] == 1:
                pygame.draw.rect(
                    janela,
                    (0, 200, 255),
                    (x, y, tamanho_celula, tamanho_celula),
                )

            else:
                pygame.draw.rect(
                    janela,
                    (80, 80, 80),
                    (x, y, tamanho_celula, tamanho_celula),
                    1,
                )


def desenhar_peca(peca):
    for linha_peca in range(len(peca.formato)):
        for coluna_peca in range(len(peca.formato[linha_peca])):

            if peca.formato[linha_peca][coluna_peca] == 1:
                x = (
                    peca.coluna + coluna_peca
                ) * tamanho_celula

                y = (
                    peca.linha + linha_peca
                ) * tamanho_celula

                pygame.draw.rect(
                    janela,
                    (0, 200, 255),
                    (x, y, tamanho_celula, tamanho_celula),
                )


def desenhar_pontuacao(pontuacao):
    texto = fonte.render(
        f"Pontos: {pontuacao}",
        True,
        (255, 255, 255),
    )

    janela.blit(texto, (270, 30))


def desenhar_game_over():
    texto = fonte.render(
        "GAME OVER",
        True,
        (255, 255, 255),
    )

    janela.blit(texto, (270, 100))

    texto_reiniciar = fonte.render(
        "R = Reiniciar",
        True,
        (255, 255, 255),
    )

    janela.blit(texto_reiniciar, (270, 140))


# -------------------------
# MOVIMENTAÇÃO
# -------------------------

def pode_mover_lado(peca, deslocamento):
    for linha_peca in range(len(peca.formato)):
        for coluna_peca in range(len(peca.formato[linha_peca])):

            if peca.formato[linha_peca][coluna_peca] == 1:
                linha_tabuleiro = peca.linha + linha_peca
                nova_coluna = (
                    peca.coluna
                    + coluna_peca
                    + deslocamento
                )

                if nova_coluna < 0 or nova_coluna >= colunas:
                    return False

                if tabuleiro[linha_tabuleiro][nova_coluna] == 1:
                    return False

    return True


def pode_descer(peca):
    for linha_peca in range(len(peca.formato)):
        for coluna_peca in range(len(peca.formato[linha_peca])):

            if peca.formato[linha_peca][coluna_peca] == 1:
                proxima_linha = (
                    peca.linha
                    + linha_peca
                    + 1
                )

                coluna_tabuleiro = (
                    peca.coluna
                    + coluna_peca
                )

                if proxima_linha >= linhas:
                    return False

                if tabuleiro[proxima_linha][coluna_tabuleiro] == 1:
                    return False

    return True


# -------------------------
# ROTAÇÃO
# -------------------------

def rotacionar_peca(formato):
    return [
        list(linha)
        for linha in zip(*formato[::-1])
    ]


def pode_rotacionar(peca_rotacionada, peca):
    for linha_peca in range(len(peca_rotacionada)):
        for coluna_peca in range(
            len(peca_rotacionada[linha_peca])
        ):

            if peca_rotacionada[linha_peca][coluna_peca] == 1:
                linha_tabuleiro = (
                    peca.linha
                    + linha_peca
                )

                coluna_tabuleiro = (
                    peca.coluna
                    + coluna_peca
                )

                if linha_tabuleiro >= linhas:
                    return False

                if coluna_tabuleiro < 0 or coluna_tabuleiro >= colunas:
                    return False

                if tabuleiro[linha_tabuleiro][coluna_tabuleiro] == 1:
                    return False

    return True


# -------------------------
# POSICIONAMENTO
# -------------------------

def pode_posicionar_peca(peca):
    for linha_peca in range(len(peca.formato)):
        for coluna_peca in range(len(peca.formato[linha_peca])):

            if peca.formato[linha_peca][coluna_peca] == 1:
                linha_tabuleiro = (
                    peca.linha
                    + linha_peca
                )

                coluna_tabuleiro = (
                    peca.coluna
                    + coluna_peca
                )

                if linha_tabuleiro < 0 or linha_tabuleiro >= linhas:
                    return False

                if coluna_tabuleiro < 0 or coluna_tabuleiro >= colunas:
                    return False

                if tabuleiro[linha_tabuleiro][coluna_tabuleiro] == 1:
                    return False

    return True


# -------------------------
# TABULEIRO
# -------------------------

def fixar_peca(peca):
    for linha_peca in range(len(peca.formato)):
        for coluna_peca in range(len(peca.formato[linha_peca])):

            if peca.formato[linha_peca][coluna_peca] == 1:
                linha_tabuleiro = (
                    peca.linha
                    + linha_peca
                )

                coluna_tabuleiro = (
                    peca.coluna
                    + coluna_peca
                )

                tabuleiro[linha_tabuleiro][coluna_tabuleiro] = 1


def remover_linhas_completas():
    linhas_restantes = []

    for linha in tabuleiro:
        if 0 in linha:
            linhas_restantes.append(linha)

    linhas_removidas = linhas - len(linhas_restantes)

    for _ in range(linhas_removidas):
        nova_linha = [0] * colunas
        linhas_restantes.insert(0, nova_linha)

    tabuleiro[:] = linhas_restantes

    return linhas_removidas


# -------------------------
# QUEDA AUTOMÁTICA
# -------------------------

def atualizar_queda(
    peca,
    tempo_ultima_queda,
    pontuacao,
    game_over,
):
    tempo_atual = pygame.time.get_ticks()

    if tempo_atual - tempo_ultima_queda >= intervalo_queda:

        if pode_descer(peca):
            peca.linha += 1

        else:
            fixar_peca(peca)

            linhas_removidas = remover_linhas_completas()

            pontuacao += linhas_removidas * 100

            peca = Peca(
                random.choice(pecas)
            )

            if not pode_posicionar_peca(peca):
                game_over = True

        tempo_ultima_queda = tempo_atual

    return (
        peca,
        tempo_ultima_queda,
        pontuacao,
        game_over,
    )


# -------------------------
# REINICIAR
# -------------------------

def reiniciar_jogo():
    novo_tabuleiro = criar_tabuleiro()

    nova_peca = Peca(
        random.choice(pecas)
    )

    nova_pontuacao = 0
    novo_game_over = False

    novo_tempo_queda = pygame.time.get_ticks()

    return (
        novo_tabuleiro,
        nova_peca,
        nova_pontuacao,
        novo_game_over,
        novo_tempo_queda,
    )


# -------------------------
# EVENTOS
# -------------------------

def processar_eventos(
    rodando,
    peca,
    game_over,
):
    reiniciar = False

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_r and game_over:
                reiniciar = True

            if not game_over:

                if evento.key == pygame.K_LEFT:
                    if pode_mover_lado(peca, -1):
                        peca.coluna -= 1

                if evento.key == pygame.K_RIGHT:
                    if pode_mover_lado(peca, 1):
                        peca.coluna += 1

                if evento.key == pygame.K_DOWN:
                    if pode_descer(peca):
                        peca.linha += 1

                if evento.key == pygame.K_UP:
                    peca_rotacionada = peca.rotacionar()

                    if pode_rotacionar(
                        peca_rotacionada,
                        peca,
                    ):
                        peca.formato = peca_rotacionada

    return rodando, peca, reiniciar


# -------------------------
# GAME LOOP
# -------------------------

while rodando:

    rodando, peca_atual, reiniciar = processar_eventos(
        rodando,
        peca_atual,
        game_over,
    )

    if reiniciar:
        (
            tabuleiro,
            peca_atual,
            pontuacao,
            game_over,
            tempo_ultima_queda,
        ) = reiniciar_jogo()

    if not game_over:
        (
            peca_atual,
            tempo_ultima_queda,
            pontuacao,
            game_over,
        ) = atualizar_queda(
            peca_atual,
            tempo_ultima_queda,
            pontuacao,
            game_over,
        )

    janela.fill((20, 20, 20))

    desenhar_tabuleiro()
    desenhar_peca(peca_atual)
    desenhar_pontuacao(pontuacao)

    if game_over:
        desenhar_game_over()

    pygame.display.update()

    clock.tick(60)


pygame.quit()