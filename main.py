import pygame

pygame.init()

largura = 400
altura = 500

janela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()  # controla FPS

linhas = 20
colunas = 10
tamanho_celula = 25


rodando = True

tabuleiro = []

for linha in range(linhas):
    nova_linha = []

    for coluna in range(colunas):
        nova_linha.append(0)

    tabuleiro.append(nova_linha)

peca_o = [[1, 1], [1, 1]]
peca_linha = 5
peca_coluna = 3

tempo_ultima_queda = pygame.time.get_ticks()
intervalo_queda = 500  # 500 milisegundos

def desenhar_tabuleiro():
    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula

            if tabuleiro[linha][coluna] == 1:
                pygame.draw.rect(
                    janela, (0, 200, 255), (x, y, tamanho_celula, tamanho_celula)
                )
            else:
                pygame.draw.rect(
                    janela, (80, 80, 80), (x, y, tamanho_celula, tamanho_celula), 1
                )

def desenhar_peca(): 
    for linha_peca in range(len(peca_o)):
        for coluna_peca in range(len(peca_o[linha_peca])):
            if peca_o[linha_peca][coluna_peca] == 1:
                x = (peca_coluna + coluna_peca) * tamanho_celula
                y = (peca_linha + linha_peca) * tamanho_celula
                pygame.draw.rect(
                    janela, (0, 200, 255), (x, y, tamanho_celula, tamanho_celula)
                )

def processar_eventos(rodando,peca_linha,peca_coluna):
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
    
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    if peca_coluna > 0:
                        peca_coluna -= 1
    
                if evento.key == pygame.K_RIGHT:
                    if peca_coluna < colunas - len(peca_o[0]):
                        peca_coluna += 1
    
                if evento.key == pygame.K_DOWN:
                    if peca_linha < linhas - len(peca_o):
                        peca_linha += 1
    return rodando,peca_linha,peca_coluna

while rodando:
    rodando,peca_linha,peca_coluna = processar_eventos(rodando,peca_linha,peca_coluna)

    tempo_atual = pygame.time.get_ticks()

    if tempo_atual - tempo_ultima_queda >= intervalo_queda:
        if peca_linha < linhas - len(peca_o):
            peca_linha += 1
        else:
            for linha_peca in range(len(peca_o)):
                for coluna_peca in range(len(peca_o[linha_peca])):
                    if peca_o[linha_peca][coluna_peca] == 1:
                        tabuleiro[peca_linha + linha_peca][peca_coluna + coluna_peca] = 1

            peca_linha = 0
            peca_coluna = (colunas - len(peca_o[0])) // 2            

        tempo_ultima_queda = tempo_atual

    janela.fill((20, 20, 20))  # cor RGB

    desenhar_tabuleiro()

    desenhar_peca()

    pygame.display.update()
    clock.tick(60)  # 60 FPS


pygame.quit()
