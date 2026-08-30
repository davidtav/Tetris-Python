import pygame

pygame.init()

largura = 800
altura = 500

janela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()  #controla FPS

linhas = 20
colunas = 10
tamanho_celula = 25


rodando = True

tabuleiro =[]

for linha in range(linhas):
    nova_linha = []

    for coluna in range(colunas):
        nova_linha.append(0)

    tabuleiro.append(nova_linha)

tabuleiro[5][3] =1

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((20,20,20)) #cor RGB

    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula

            if tabuleiro[linha][coluna] == 1:
                pygame.draw.rect(
                    janela,
                    (0,200,255),
                    (x,y,tamanho_celula,tamanho_celula)
                )
            else:
                pygame.draw.rect(
                janela,
                (80,80,80),
                (x,y,tamanho_celula,tamanho_celula),
                1
            )      
    
    pygame.display.update()
    clock.tick(60)       #60 FPS   



pygame.quit()